# --- DEEL 1 ---

import copy
import random
import pygame
import math

pygame.font.init()
pygame.mixer.init()

BASE_WIDTH = 600
BASE_HEIGHT = 900

screen = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT), pygame.RESIZABLE)
WIDTH, HEIGHT = screen.get_size()

pygame.display.set_caption('Pygame Blackjack!')
fps = 60
timer = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 44)
btn_font = pygame.font.Font('freesansbold.ttf', 32)
smaller_font = pygame.font.Font('freesansbold.ttf', 30)

active = False

cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A','SJ']
one_deck = 4 * cards
decks = 4

records = [0, 0, 0]
player_score = 0
dealer_score = 0
initial_deal = False
my_hand = []
dealer_hand = []
outcome = 0
reveal_dealer = False
hand_active = False
add_score = False

results = [
    '',
    'PLAYER BUSTED!',
    'PLAYER WINS!',
    'FRED WINS!',
    'TIE GAME'
]

CARD_W = 120
CARD_H = 220
OVERLAP = 50

sound_flip = pygame.mixer.Sound("sounds/flip.mp3")
sound_win = pygame.mixer.Sound("sounds/win.mp3")
sound_lose = pygame.mixer.Sound("sounds/lose.mp3")
sound_draw = pygame.mixer.Sound("sounds/draw.mp3")
sound_superjoker = pygame.mixer.Sound("sounds/superjoker.mp3")

played_win = False
played_lose = False
played_draw = False

animated_cards = []

background = pygame.transform.scale(pygame.image.load('images/achtergrond.png'), (WIDTH, HEIGHT))
startscreen = pygame.transform.scale(pygame.image.load('images/startscreen.png'), (WIDTH, HEIGHT))

card_back = pygame.transform.smoothscale(pygame.image.load('images/frederik.png'), (CARD_W, CARD_H))

card_images = {}
for value in cards:
    img = pygame.image.load(f'images/kaarten/{value}.png').convert_alpha()
    img = pygame.transform.smoothscale(img, (CARD_W, CARD_H))
    card_images[value] = img


def draw_gold_frame():
    border = 4
    color_outer = (200, 170, 0)
    color_inner = (30, 30, 30)
    pygame.draw.rect(screen, color_outer, (0, 0, WIDTH, HEIGHT), border, 25)
    pygame.draw.rect(screen, color_inner, (border, border, WIDTH - 2*border, HEIGHT - 2*border), 2, 20)


def draw_3d_shadow(x, y):
    shadow = pygame.Surface((CARD_W + 40, CARD_H + 40), pygame.SRCALPHA)
    pygame.draw.ellipse(shadow, (0, 0, 0, 120), (0, 0, CARD_W + 40, 40))
    screen.blit(shadow, (x - 20, y + CARD_H - 10))


def draw_card_with_frame(image, x, y, pulse_strength=0, glow=False, red_glow=False):
    gold = (200 + pulse_strength, 170 + pulse_strength, 0)

    if red_glow:
        glow_surf = pygame.Surface((CARD_W + 40, CARD_H + 40), pygame.SRCALPHA)
        pygame.draw.rect(glow_surf, (255, 0, 0, 140), (0, 0, CARD_W + 40, CARD_H + 40), border_radius=25)
        screen.blit(glow_surf, (x - 20, y - 20))

    if glow:
        glow_surf = pygame.Surface((CARD_W + 30, CARD_H + 30), pygame.SRCALPHA)
        pygame.draw.rect(glow_surf, (255, 215, 0, 120), (0, 0, CARD_W + 30, CARD_H + 30), border_radius=20)
        screen.blit(glow_surf, (x - 15, y - 15))

    pygame.draw.rect(screen, gold, (x - 3, y - 3, CARD_W + 6, CARD_H + 6), border_radius=8)
    pygame.draw.rect(screen, (20, 20, 20), (x - 1, y - 1, CARD_W + 2, CARD_H + 2), border_radius=6)
    screen.blit(image, (x, y))


def draw_gold_message(text):
    msg_font = pygame.font.Font('freesansbold.ttf', 42)
    y = int(HEIGHT * 0.13)

    shadow = msg_font.render(text, True, (0, 0, 0))
    screen.blit(shadow, shadow.get_rect(center=(WIDTH // 2 + 4, y + 4)))

    gold = msg_font.render(text, True, (255, 215, 0))
    screen.blit(gold, gold.get_rect(center=(WIDTH // 2, y)))


def draw_superjoker_message():
    msg_font = pygame.font.Font('freesansbold.ttf', 32)
    text = "SUPER JOKER – FRED WINS!"
    y = int(HEIGHT * 0.13)

    shadow = msg_font.render(text, True, (0, 0, 0))
    screen.blit(shadow, shadow.get_rect(center=(WIDTH // 2 + 4, y + 4)))

    gold = msg_font.render(text, True, (255, 215, 0))
    screen.blit(gold, gold.get_rect(center=(WIDTH // 2, y)))


class AnimatedCard:
    def __init__(self, image, start_pos, end_pos, speed=25, value=None, is_dealer=False, index=0):
        self.image = image
        self.x, self.y = start_pos
        self.end_x, self.end_y = end_pos
        self.speed = speed
        self.done = False
        self.pulse_timer = 0
        self.value = value
        self.revealed = False
        self.is_dealer = is_dealer
        self.index = index

    def update(self):
        if self.done:
            return
        if abs(self.x - self.end_x) > self.speed:
            self.x += self.speed if self.x < self.end_x else -self.speed
        else:
            self.x = self.end_x
        if abs(self.y - self.end_y) > self.speed:
            self.y += self.speed if self.y < self.end_y else -self.speed
        else:
            self.y = self.end_y
        if self.x == self.end_x and self.y == self.end_y:
            self.done = True
            self.revealed = True
            self.pulse_timer = 12

    def draw(self):
        draw_3d_shadow(self.x, self.y)
        pulse_strength = 0
        if self.pulse_timer > 0:
            pulse_strength = int(80 * math.sin(self.pulse_timer / 12 * math.pi))
            self.pulse_timer -= 1

        is_joker = (self.value == 'SJ')
        draw_card_with_frame(self.image, self.x, self.y, pulse_strength, red_glow=is_joker)

def deal_card_with_animation(hand, deck, is_player):
    global outcome, hand_active, reveal_dealer, played_lose, add_score

    card = deck[random.randint(0, len(deck)-1)]

    if not is_player:
        while card == 'SJ':
            card = deck[random.randint(0, len(deck)-1)]

    hand.append(card)
    deck.remove(card)

    if is_player and card == 'SJ':
        sound_superjoker.play()

        outcome = 3
        hand_active = False
        reveal_dealer = True

        if not played_lose:
            sound_lose.play()
            played_lose = True

        if add_score:
            records[1] += 1
            add_score = False

        return

    index = len(hand) - 1
    end_x = 70 + (OVERLAP * index)
    end_y = (460 if is_player else 160) + (5 * index)

    animated_cards.append(
        AnimatedCard(
            card_images[card],
            start_pos=(WIDTH//2, -250),
            end_pos=(end_x, end_y),
            speed=25,
            value=card,
            is_dealer=not is_player,
            index=index
        )
    )

    sound_flip.play()


def calculate_score(hand):
    score = 0
    aces = hand.count('A')
    for card in hand:
        if card == 'SJ':
            score += 0
        elif card in ['10','J','Q','K']:
            score += 10
        elif card == 'A':
            score += 11
        else:
            score += int(card)
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score


def draw_value_badges(player, dealer, reveal):
    rect_p = [WIDTH - 220, 460, 200, 60]
    pygame.draw.rect(screen, (30, 30, 30), rect_p, 0, 15)
    pygame.draw.rect(screen, (200, 170, 0), rect_p, 4, 15)
    p_text = smaller_font.render(f"Player: {player}", True, (255, 215, 0))
    screen.blit(p_text, p_text.get_rect(center=(rect_p[0] + 100, rect_p[1] + 30)))

    rect_d = [WIDTH - 220, 160, 200, 60]
    pygame.draw.rect(screen, (30, 30, 30), rect_d, 0, 15)
    pygame.draw.rect(screen, (200, 170, 0), rect_d, 4, 15)

    if not reveal:
        visible = dealer_hand[1] if len(dealer_hand) > 1 else dealer_hand[0]
        visible_value = 10 if visible in ['10','J','Q','K'] else (11 if visible == 'A' else 0 if visible == 'SJ' else int(visible))
        d_text = smaller_font.render(f"Fred: {visible_value}", True, (255, 215, 0))
    else:
        d_text = smaller_font.render(f"Fred: {dealer}", True, (255, 215, 0))

    screen.blit(d_text, d_text.get_rect(center=(rect_d[0] + 100, rect_d[1] + 30)))


def draw_record_badge(records):
    text = f"Wins: {records[0]}   Losses: {records[1]}   Draws: {records[2]}"
    rendered = smaller_font.render(text, True, (255, 215, 0))
    screen.blit(rendered, rendered.get_rect(center=(WIDTH // 2, 40)))


def draw_cards(player, dealer, reveal):
    blackjack_glow = (len(player) == 2 and calculate_score(player) == 21)

    for i, card in enumerate(player):
        x = 70 + (OVERLAP * i)
        y = 460 + (5 * i)
        anim = next((c for c in animated_cards if c.value == card and not c.is_dealer and c.index == i), None)
        if anim and not anim.revealed:
            continue
        is_joker = (card == 'SJ')
        draw_card_with_frame(card_images[card], x, y, glow=blackjack_glow, red_glow=is_joker)

    for i, card in enumerate(dealer):
        x = 70 + (OVERLAP * i)
        y = 160 + (5 * i)
        anim = next((c for c in animated_cards if c.value == card and c.is_dealer and c.index == i), None)
        if anim and not anim.revealed:
            continue
        if i == 0 and not reveal:
            draw_card_with_frame(card_back, x, y)
        else:
            is_joker = (card == 'SJ')
            draw_card_with_frame(card_images[card], x, y, red_glow=is_joker)


def draw_centered_text(surface, text, rect, font, color):
    rendered = font.render(text, True, color)
    surface.blit(rendered, rendered.get_rect(center=(rect[0] + rect[2]//2, rect[1] + rect[3]//2)))


def draw_game(act, record, result):
    button_list = []

    if not act:
        rect = [WIDTH//2 - 150, HEIGHT - 250, 300, 120]
        start_btn = pygame.draw.rect(screen, (30, 30, 30), rect, 0, 25)
        pygame.draw.rect(screen, (200, 170, 0), rect, 5, 25)
        draw_centered_text(screen, "START GAME", rect, btn_font, (255, 215, 0))
        button_list.append(start_btn)

    else:
        rect_hit = [20, HEIGHT - 180, 160, 80]
        hit_btn = pygame.draw.rect(screen, (30, 30, 30), rect_hit, 0, 25)
        pygame.draw.rect(screen, (200, 170, 0), rect_hit, 5, 25)
        draw_centered_text(screen, "HIT ME", rect_hit, btn_font, (255, 215, 0))
        button_list.append(hit_btn)

        rect_stand = [WIDTH - 180, HEIGHT - 180, 160, 80]
        stand_btn = pygame.draw.rect(screen, (30, 30, 30), rect_stand, 0, 25)
        pygame.draw.rect(screen, (200, 170, 0), rect_stand, 5, 25)
        draw_centered_text(screen, "STAND", rect_stand, btn_font, (255, 215, 0))
        button_list.append(stand_btn)

    if result != 0:
        if result == 3 and any(c == 'SJ' for c in my_hand):
            draw_superjoker_message()
        else:
            draw_gold_message(results[result])

        rect_new = [WIDTH//2 - 100, HEIGHT - 180, 200, 80]
        new_btn = pygame.draw.rect(screen, (30, 30, 30), rect_new, 0, 25)
        pygame.draw.rect(screen, (200, 170, 0), rect_new, 5, 25)
        draw_centered_text(screen, "NEW HAND", rect_new, btn_font, (255, 215, 0))
        button_list.append(new_btn)

    return button_list


def check_endgame(hand_act, deal_score, play_score, result, totals, add):
    global played_win, played_lose, played_draw

    if not hand_act and deal_score >= 17:
        if play_score > 21:
            result = 1
            if not played_lose:
                sound_lose.play()
                played_lose = True
        elif deal_score < play_score <= 21 or dealer_score > 21:
            result = 2
            if not played_win:
                sound_win.play()
                played_win = True
        elif play_score < deal_score <= 21:
            result = 3
            if not played_lose:
                sound_lose.play()
                played_lose = True
        else:
            result = 4
            if not played_draw:
                sound_draw.play()
                played_draw = True

        if add:
            if result in [1, 3]:
                totals[1] += 1
            elif result == 2:
                totals[0] += 1
            else:
                totals[2] += 1
            add = False

    return result, totals, add

run = True
buttons = [pygame.Rect(0, 0, 0, 0)]

while run:
    timer.tick(fps)

    if not active:
        screen.blit(startscreen, (0, 0))
    else:
        screen.blit(background, (0, 0))

    draw_gold_frame()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            background = pygame.transform.scale(pygame.image.load('images/achtergrond.png'), (WIDTH, HEIGHT))
            startscreen = pygame.transform.scale(pygame.image.load('images/startscreen.png'), (WIDTH, HEIGHT))

        if event.type == pygame.MOUSEBUTTONUP:
            if not active:
                if buttons and buttons[0].collidepoint(event.pos):
                    active = True
                    initial_deal = True
                    game_deck = copy.deepcopy(decks * one_deck)
                    my_hand = []
                    dealer_hand = []
                    outcome = 0
                    hand_active = True
                    reveal_dealer = False
                    add_score = True
                    played_win = played_lose = played_draw = False

            else:
                if len(buttons) >= 1 and buttons[0].collidepoint(event.pos) and player_score < 21 and hand_active:
                    deal_card_with_animation(my_hand, game_deck, True)

                elif len(buttons) >= 2 and buttons[1].collidepoint(event.pos) and not reveal_dealer:
                    reveal_dealer = True
                    hand_active = False

                elif len(buttons) == 3 and buttons[2].collidepoint(event.pos):
                    active = True
                    initial_deal = True
                    game_deck = copy.deepcopy(decks * one_deck)
                    my_hand = []
                    dealer_hand = []
                    outcome = 0
                    hand_active = True
                    reveal_dealer = False
                    add_score = True
                    dealer_score = player_score = 0
                    played_win = played_lose = played_draw = False

    if initial_deal:
        for _ in range(2):
            deal_card_with_animation(my_hand, game_deck, True)
            deal_card_with_animation(dealer_hand, game_deck, False)
        initial_deal = False

    if active:
        player_score = calculate_score(my_hand)
        draw_cards(my_hand, dealer_hand, reveal_dealer)
        draw_value_badges(player_score, dealer_score, reveal_dealer)
        draw_record_badge(records)

        if reveal_dealer:
            dealer_score = calculate_score(dealer_hand)
            if dealer_score < 17 and outcome == 0:
                deal_card_with_animation(dealer_hand, game_deck, False)

    for card in animated_cards:
        card.update()
        card.draw()

    animated_cards = [c for c in animated_cards if not c.done]

    buttons = draw_game(active, records, outcome)

    if hand_active and player_score >= 21:
        hand_active = False
        reveal_dealer = True

    outcome, records, add_score = check_endgame(
        hand_active, dealer_score, player_score, outcome, records, add_score
    )

    pygame.display.flip()

pygame.quit()
