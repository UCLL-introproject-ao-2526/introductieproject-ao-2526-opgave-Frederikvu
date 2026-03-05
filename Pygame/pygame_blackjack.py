# ============================================================
# Project: Pygame Blackjack
# Auteur: Frederik (Optimized for Laptop)
# Omschrijving: Een volledig grafisch Blackjack-spel met animaties,
#               geluidseffecten, Super Joker-regel en dynamische UI.
# ============================================================

import copy
import random
import pygame
import math

# Initialisatie
pygame.font.init()
pygame.mixer.init()

# Aangepaste afmetingen voor laptop schermen
BASE_WIDTH = 600
BASE_HEIGHT = 800 

screen = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT), pygame.RESIZABLE)
WIDTH, HEIGHT = screen.get_size()

pygame.display.set_caption('Pygame Blackjack!')
fps = 60
timer = pygame.time.Clock()

# Fonts
font = pygame.font.Font('freesansbold.ttf', 44)
btn_font = pygame.font.Font('freesansbold.ttf', 32)
smaller_font = pygame.font.Font('freesansbold.ttf', 26) 
help_font = pygame.font.Font('freesansbold.ttf', 14)

# Spelvariabelen
active = False
show_help = False
dealer_draw_timer = 0 # Timer voor dealer vertraging

cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A','SJ']
one_deck = 4 * cards
decks = 4

records = [0, 0, 0] # Wins, Losses, Draws
player_score = 0
dealer_score = 0
initial_deal = False
my_hand = []
dealer_hand = []
outcome = 0
reveal_dealer = False
hand_active = False
add_score = False

results = ['', 'PLAYER BUSTED!', 'PLAYER WINS!', 'FRED WINS!', 'TIE GAME']

# Kaart afmetingen
CARD_W = 105
CARD_H = 185
OVERLAP = 45

# ============================================================
# Geluiden & Afbeeldingen
# ============================================================

bg_orig = pygame.image.load('images/achtergrond.png')
start_orig = pygame.image.load('images/startscreen.png')

background = pygame.transform.scale(bg_orig, (WIDTH, HEIGHT))
startscreen = pygame.transform.scale(start_orig, (WIDTH, HEIGHT))

sound_flip = pygame.mixer.Sound("sounds/flip.mp3")
sound_win = pygame.mixer.Sound("sounds/win.mp3")
sound_lose = pygame.mixer.Sound("sounds/lose.mp3")
sound_draw = pygame.mixer.Sound("sounds/draw.mp3")
sound_superjoker = pygame.mixer.Sound("sounds/superjoker.mp3")

played_win = False
played_lose = False
played_draw = False

animated_cards = []

card_back = pygame.transform.smoothscale(pygame.image.load('images/frederik.png'), (CARD_W, CARD_H))

card_images = {}
for value in cards:
    img = pygame.image.load(f'images/kaarten/{value}.png').convert_alpha()
    img = pygame.transform.smoothscale(img, (CARD_W, CARD_H))
    card_images[value] = img

# ============================================================
# UI & Tekenfuncties
# ============================================================

def draw_gold_frame():
    border = 4
    color_outer = (200, 170, 0)
    color_inner = (30, 30, 30)
    pygame.draw.rect(screen, color_outer, (0, 0, WIDTH, HEIGHT), border, 25)
    pygame.draw.rect(screen, color_inner, (border, border, WIDTH - 2*border, HEIGHT - 2*border), 2, 20)

def draw_3d_shadow(x, y):
    shadow = pygame.Surface((CARD_W + 30, 40), pygame.SRCALPHA)
    pygame.draw.ellipse(shadow, (0, 0, 0, 100), (0, 0, CARD_W + 30, 30))
    screen.blit(shadow, (x - 15, y + CARD_H - 10))

def draw_card_with_frame(image, x, y, pulse_strength=0, glow=False, red_glow=False):
    gold = (min(255, 200 + pulse_strength), min(255, 170 + pulse_strength), 0)
    if red_glow:
        glow_surf = pygame.Surface((CARD_W + 30, CARD_H + 30), pygame.SRCALPHA)
        pygame.draw.rect(glow_surf, (255, 0, 0, 140), (0, 0, CARD_W + 30, CARD_H + 30), border_radius=20)
        screen.blit(glow_surf, (x - 15, y - 15))
    if glow:
        glow_surf = pygame.Surface((CARD_W + 20, CARD_H + 20), pygame.SRCALPHA)
        pygame.draw.rect(glow_surf, (255, 215, 0, 120), (0, 0, CARD_W + 20, CARD_H + 20), border_radius=15)
        screen.blit(glow_surf, (x - 10, y - 10))
    pygame.draw.rect(screen, gold, (x - 3, y - 3, CARD_W + 6, CARD_H + 6), border_radius=8)
    pygame.draw.rect(screen, (20, 20, 20), (x - 1, y - 1, CARD_W + 2, CARD_H + 2), border_radius=6)
    screen.blit(image, (x, y))

def draw_gold_message(text):
    msg_font = pygame.font.Font('freesansbold.ttf', 38)
    y = int(HEIGHT * 0.12)
    shadow = msg_font.render(text, True, (0, 0, 0))
    screen.blit(shadow, shadow.get_rect(center=(WIDTH // 2 + 3, y + 3)))
    gold = msg_font.render(text, True, (255, 215, 0))
    screen.blit(gold, gold.get_rect(center=(WIDTH // 2, y)))

def draw_superjoker_message():
    msg_font = pygame.font.Font('freesansbold.ttf', 32)
    text = "SUPER JOKER – FRED WINS!"
    y = int(HEIGHT * 0.12)
    shadow = msg_font.render(text, True, (0, 0, 0))
    screen.blit(shadow, shadow.get_rect(center=(WIDTH // 2 + 3, y + 3)))
    gold = msg_font.render(text, True, (255, 215, 0))
    screen.blit(gold, gold.get_rect(center=(WIDTH // 2, y)))

def draw_help_screen():
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 220))
    screen.blit(overlay, (0, 0))
    lines = [
        "HANDLEIDING", "",
        "Dit spel is een Blackjack-variant met een speciale Super Joker-regel!",
        "Speciale regel:",
        "- Super Joker (SJ): als deze kaart valt, verliest de speler automatisch.",
        "Klik op START GAME om het spel te beginnen.",
        "Klik op HIT ME: neem een extra kaart.",
        "Klik op STAND: stop met kaarten nemen.",
        "Klik op NEW HAND om opnieuw te spelen.",
        "Klik op ESC om spel af te sluiten",
        "Klik op CLOSE om terug te keren."
    ]
    y = 150
    for line in lines:
        text = help_font.render(line, True, (255, 215, 0))
        screen.blit(text, text.get_rect(center=(WIDTH//2, y)))
        y += 40
    close_rect = pygame.Rect(WIDTH//2 - 80, HEIGHT - 120, 160, 60)
    pygame.draw.rect(screen, (30, 30, 30), close_rect, 0, 20)
    pygame.draw.rect(screen, (200, 170, 0), close_rect, 4, 20)
    draw_centered_text(screen, "CLOSE", close_rect, btn_font, (255, 215, 0))
    return close_rect

# ============================================================
# UI: Waardes, Records, Kaarten & Knoppen
# ============================================================

def draw_value_badges(player, dealer, reveal):
    p_badge_y = int(HEIGHT * 0.52)
    d_badge_y = int(HEIGHT * 0.18)
    rect_p = [WIDTH - 190, p_badge_y, 170, 50]
    pygame.draw.rect(screen, (30, 30, 30), rect_p, 0, 15)
    pygame.draw.rect(screen, (200, 170, 0), rect_p, 3, 15)
    p_text = smaller_font.render(f"Speler: {player}", True, (255, 215, 0))
    screen.blit(p_text, p_text.get_rect(center=(rect_p[0] + 85, rect_p[1] + 25)))
    rect_d = [WIDTH - 190, d_badge_y, 170, 50]
    pygame.draw.rect(screen, (30, 30, 30), rect_d, 0, 15)
    pygame.draw.rect(screen, (200, 170, 0), rect_d, 3, 15)
    if not reveal and len(dealer_hand) > 0:
        visible = dealer_hand[1] if len(dealer_hand) > 1 else dealer_hand[0]
        v_val = 10 if visible in ['10','J','Q','K'] else (11 if visible == 'A' else 0 if visible == 'SJ' else int(visible))
        d_text = smaller_font.render(f"Fred: {v_val}", True, (255, 215, 0))
    else:
        d_text = smaller_font.render(f"Fred: {dealer}", True, (255, 215, 0))
    screen.blit(d_text, d_text.get_rect(center=(rect_d[0] + 85, rect_d[1] + 25)))

def draw_record_badge(records):
    text = f"Wins: {records[0]}   Losses: {records[1]}   Draws: {records[2]}"
    rendered = smaller_font.render(text, True, (255, 215, 0))
    screen.blit(rendered, rendered.get_rect(center=(WIDTH // 2, 40)))

def draw_cards(player, dealer, reveal):
    blackjack_glow = (len(player) == 2 and calculate_score(player) == 21)
    p_start_y = int(HEIGHT * 0.52)
    d_start_y = int(HEIGHT * 0.18)
    for i, card in enumerate(player):
        x, y = 60 + (OVERLAP * i), p_start_y + (5 * i)
        if any(c.value == card and not c.is_dealer and c.index == i and not c.revealed for c in animated_cards): continue
        draw_card_with_frame(card_images[card], x, y, glow=blackjack_glow, red_glow=(card == 'SJ'))
    for i, card in enumerate(dealer):
        x, y = 60 + (OVERLAP * i), d_start_y + (5 * i)
        if any(c.value == card and c.is_dealer and c.index == i and not c.revealed for c in animated_cards): continue
        if i == 0 and not reveal:
            draw_card_with_frame(card_back, x, y)
        else:
            draw_card_with_frame(card_images[card], x, y, red_glow=(card == 'SJ'))

def draw_centered_text(surface, text, rect, font, color):
    rendered = font.render(text, True, color)
    surface.blit(rendered, rendered.get_rect(center=(rect[0] + rect[2]//2, rect[1] + rect[3]//2)))

def draw_game(act, record, result):
    button_list = []
    if not act:
        rect = pygame.Rect(WIDTH//2 - 120, HEIGHT//2 - 50, 240, 100)
        pygame.draw.rect(screen, (30, 30, 30), rect, 0, 25)
        pygame.draw.rect(screen, (200, 170, 0), rect, 5, 25)
        draw_centered_text(screen, "START GAME", rect, btn_font, (255, 215, 0))
        button_list.append(rect)
        help_rect = pygame.Rect(WIDTH//2 - 60, HEIGHT - 90, 120, 50)
        pygame.draw.rect(screen, (30, 30, 30), help_rect, 0, 15)
        pygame.draw.rect(screen, (200, 170, 0), help_rect, 3, 15)
        draw_centered_text(screen, "HELP", help_rect, smaller_font, (255, 215, 0))
        button_list.append(help_rect)
    else:
        rect_hit = pygame.Rect(30, HEIGHT - 110, 140, 70)
        pygame.draw.rect(screen, (30, 30, 30), rect_hit, 0, 20)
        pygame.draw.rect(screen, (200, 170, 0), rect_hit, 4, 20)
        draw_centered_text(screen, "HIT ME", rect_hit, btn_font, (255, 215, 0))
        button_list.append(rect_hit)

        rect_stand = pygame.Rect(WIDTH - 170, HEIGHT - 110, 140, 70)
        pygame.draw.rect(screen, (30, 30, 30), rect_stand, 0, 20)
        pygame.draw.rect(screen, (200, 170, 0), rect_stand, 4, 20)
        draw_centered_text(screen, "STAND", rect_stand, btn_font, (255, 215, 0))
        button_list.append(rect_stand)

        if result != 0:
            if result == 3 and any(c == 'SJ' for c in my_hand):
                draw_superjoker_message()
            else:
                draw_gold_message(results[result])
            # Breder gemaakt: 220px
            rect_new = pygame.Rect(WIDTH//2 - 110, HEIGHT - 110, 220, 70)
            pygame.draw.rect(screen, (30, 30, 30), rect_new, 0, 20)
            pygame.draw.rect(screen, (200, 170, 0), rect_new, 4, 20)
            draw_centered_text(screen, "NEW HAND", rect_new, btn_font, (255, 215, 0))
            button_list.append(rect_new)
    return button_list

# ============================================================
# Klasse: AnimatedCard
# ============================================================

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
        if self.done: return
        dx, dy = self.end_x - self.x, self.end_y - self.y
        dist = math.hypot(dx, dy)
        if dist > self.speed:
            self.x += self.speed * (dx/dist)
            self.y += self.speed * (dy/dist)
        else:
            self.x, self.y = self.end_x, self.end_y
            self.done = True
            self.revealed = True
            self.pulse_timer = 12

    def draw(self):
        draw_3d_shadow(self.x, self.y)
        pulse = int(60 * math.sin(self.pulse_timer / 12 * math.pi)) if self.pulse_timer > 0 else 0
        if self.pulse_timer > 0: self.pulse_timer -= 1
        draw_card_with_frame(self.image, self.x, self.y, pulse, red_glow=(self.value == 'SJ'))

# ============================================================
# Spelmechanics
# ============================================================

def deal_card_with_animation(hand, deck, is_player):
    global outcome, hand_active, reveal_dealer, played_lose, add_score
    if not deck: return
    card = random.choice(deck)
    if not is_player:
        while card == 'SJ': card = random.choice(deck)
    hand.append(card)
    deck.remove(card)

    if is_player and card == 'SJ':
        sound_superjoker.play()
        outcome, hand_active, reveal_dealer, add_score = 3, False, True, True
        if not played_lose: 
            sound_lose.play()
            played_lose = True

    index = len(hand) - 1
    ex = 60 + (OVERLAP * index)
    ey = (int(HEIGHT * 0.52) if is_player else int(HEIGHT * 0.18)) + (5 * index)
    animated_cards.append(AnimatedCard(card_images[card], (WIDTH//2, -250), (ex, ey), 25, card, not is_player, index))
    sound_flip.play()

def calculate_score(hand):
    score, aces = 0, hand.count('A')
    for card in hand:
        if card == 'SJ': continue
        elif card in ['10','J','Q','K']: score += 10
        elif card == 'A': score += 11
        else: score += int(card)
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def check_endgame(hand_act, d_score, p_score, res, totals, add):
    global played_win, played_lose, played_draw
    # Als er al een resultaat is (zoals SJ), verwerk dan alleen de score
    if res != 0 and add:
        if res in [1, 3]: totals[1] += 1
        elif res == 2: totals[0] += 1
        else: totals[2] += 1
        return res, totals, False

    if not hand_act and d_score >= 17:
        if p_score > 21: res = 1
        elif d_score < p_score <= 21 or d_score > 21: res = 2
        elif p_score < d_score <= 21: res = 3
        else: res = 4
        if not any([played_win, played_lose, played_draw]):
            if res == 2: sound_win.play(); played_win = True
            elif res in [1, 3]: sound_lose.play(); played_lose = True
            else: sound_draw.play(); played_draw = True
        if add:
            if res in [1, 3]: totals[1] += 1
            elif res == 2: totals[0] += 1
            else: totals[2] += 1
            add = False
    return res, totals, add

# ============================================================
# Main Game Loop
# ============================================================

run = True
buttons = []
game_deck = copy.deepcopy(decks * one_deck)

while run:
    timer.tick(fps)
    screen.blit(background if active else startscreen, (0, 0))
    draw_gold_frame()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: run = False
        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            background = pygame.transform.scale(bg_orig, (WIDTH, HEIGHT))
            startscreen = pygame.transform.scale(start_orig, (WIDTH, HEIGHT))

        if event.type == pygame.MOUSEBUTTONUP:
            if show_help:
                if draw_help_screen().collidepoint(event.pos): show_help = False
                continue
            if not active:
                if buttons and buttons[0].collidepoint(event.pos):
                    active, initial_deal, game_deck = True, True, copy.deepcopy(decks * one_deck)
                    my_hand, dealer_hand, outcome, hand_active, reveal_dealer, add_score = [], [], 0, True, False, True
                    played_win = played_lose = played_draw = False
                elif len(buttons) > 1 and buttons[1].collidepoint(event.pos): show_help = True
            else:
                if len(buttons) >= 2:
                    if buttons[0].collidepoint(event.pos) and hand_active and player_score < 21:
                        deal_card_with_animation(my_hand, game_deck, True)
                    elif buttons[1].collidepoint(event.pos) and not reveal_dealer:
                        reveal_dealer, hand_active = True, False
                    elif len(buttons) == 3 and buttons[2].collidepoint(event.pos):
                        initial_deal, game_deck = True, copy.deepcopy(decks * one_deck)
                        my_hand, dealer_hand, outcome, hand_active, reveal_dealer, add_score = [], [], 0, True, False, True
                        dealer_score = player_score = 0
                        played_win = played_lose = played_draw = False

    if initial_deal and not animated_cards:
        if len(my_hand) < 2:
            deal_card_with_animation(my_hand, game_deck, True)
            deal_card_with_animation(dealer_hand, game_deck, False)
        else: initial_deal = False

    if active:
        player_score = calculate_score(my_hand)
        draw_cards(my_hand, dealer_hand, reveal_dealer)
        draw_value_badges(player_score, dealer_score, reveal_dealer)
        draw_record_badge(records)
        if reveal_dealer and not initial_deal:
            dealer_score = calculate_score(dealer_hand)
            if dealer_score < 17 and outcome == 0 and not animated_cards:
                if pygame.time.get_ticks() > dealer_draw_timer:
                    deal_card_with_animation(dealer_hand, game_deck, False)
                    dealer_draw_timer = pygame.time.get_ticks() + 1000 

    for card in animated_cards:
        card.update(); card.draw()
    animated_cards = [c for c in animated_cards if not c.revealed or c.pulse_timer > 0]

    buttons = draw_game(active, records, outcome)
    if hand_active and player_score >= 21:
        hand_active, reveal_dealer = False, True
    
    outcome, records, add_score = check_endgame(hand_active, dealer_score, player_score, outcome, records, add_score)
    if show_help: draw_help_screen()
    pygame.display.flip()

pygame.quit()