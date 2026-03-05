**logboek scratch Blackjack update**



doelen

**1. achtergrond dealer kaart aanpassen: OK**

**2. voorkant kaarten aanpassen: OK**

**3. zwarte achtergrond aanpassen: OK**

**4. geluid toevoegen: OK**

**5. kaart animaties toevoegen: OK**

**6. kleuren rand aanpassen: verwijderd, was niet mooi: OK**

**7. new hand aanpassen: OK**

**8. aanduiding scores aanpassen: OK**

**9. knoppen aanpassen: OK**

**10. begin scherm aanpassen -> logo + naam spel: OK**

**11. kleine variant, de (F)RedJoker als die kaart valt, dan wint de dealer (Fred) automatisch: OK**

**12. kader rond spel: OK**



02/03/2026 19:30 gestart met de update van blackjack.



* dank zij hulp van CoPilot aan de slag gegaan, de code via AI laten schrijven en zelf aangepast in mijn broncode.
* de achtergrond dealer card, is goed gelukt
* de voorkant van de speelkaarten heb ik door ChatGTP laten ontwerpen, resultaat is goed. 
* echter is de geleurde rand niet mooi op de kaarten, deze heb ik verwijderd
* de zwarte achtergrond heb ik vervangen door een gekleurde achtergrond
* 4 geluidseffecten toegevoegd: win, lose, draw en flip
* probleem geluid bij win en lose zat in loop en bleef herhalen, dit vind ik vervelend, code aangepast zodat het geluid slechts 1 x afgespeeld wordt



03/03/2026 18:00 vervolg update van blackjack

doel vandaag: 

* startscherm veranderen, 
* grootte spel automatisch aanpassen aan schermgrootte,
* aanduiding scores verbeteren,
* berichten op scherm veranderen bij win, lose en draw
* naam dealer veranderen
* (F)RedJoker in hett spel gebracht, als deze kaart valt, wint dealer Fred













🎨 Visuele verbeteringen

1\. Grote kaartafbeeldingen (120×220)

Je gebruikte eerst tekstkaarten → vervangen door echte PNG‑kaarten.



Kaarten worden automatisch geladen uit images/kaarten/.



Schaal naar een professioneel formaat (120×220).



2\. Overlappende kaarten zoals in echte casino’s

Originele spacing (70 px) was te klein voor grote kaarten.



We hebben overlap ingesteld op 50 px, zodat kaarten:



* groot blijven,
* mooi overlappen,
* volledig zichtbaar blijven.



3\. Schaduwen onder kaarten

Elke kaart krijgt een subtiele schaduw (Surface met alpha).



Hierdoor lijken kaarten te zweven boven de tafel.



Geeft een veel professionelere look.



4\. Geen randen meer rond kaarten

De rode en blauwe randen zijn verwijderd.



Enkel de kaartafbeelding + schaduw blijft zichtbaar.



5\. Achtergrondafbeelding

achtergrond.jpg wordt fullscreen geschaald.



Geeft een echte blackjack‑tafel vibe.



6\. Custom backside voor dealer

frederik.png wordt gebruikt als de omgedraaide dealerkaart.



Past perfect bij jouw persoonlijke stijl.



🔊 Geluid \& audio‑logica

7\. Flip‑geluid bij het delen van kaarten

flip.wav speelt telkens wanneer een kaart wordt gedeeld.



Zowel bij speler als dealer.



8\. Win‑geluid en lose‑geluid

win.wav speelt wanneer speler wint.



lose.wav speelt wanneer dealer wint of speler bust.



9\. Geluid speelt maar één keer (belangrijk!)

We hebben twee flags toegevoegd:



played\_win



played\_lose



Deze zorgen ervoor dat win/lose geluid niet in een loop blijft spelen.



Flags worden gereset bij elke nieuwe hand.



🧠 Code‑structuur \& logica

10\. Volledige integratie van alle features

Alles is verwerkt in jouw originele code‑structuur.



Geen logica herschreven, enkel uitgebreid.



Alle functies blijven herkenbaar en overzichtelijk.



11\. Dealer‑logica blijft identiek

Dealer trekt kaarten tot 17.



Scoreberekening blijft exact zoals je originele code.



12\. Resultaat‑afhandeling verbeterd

Win/lose geluid wordt correct getriggerd.



Resultaat wordt maar één keer verwerkt.



🎯 Wat je nu hebt

Je hebt nu een blackjack‑game die:

* professioneel oogt
* vloeiend speelt
* mooie overlap‑kaarten toont
* geluidseffecten heeft zoals in echte casino’s
* geen herhalende geluiden meer heeft
* een custom backside en achtergrond gebruikt
* volledig gebaseerd blijft op jouw originele code



-> Het is echt een grote sprong vooruit — je project ziet er nu uit als een volwaardige game.









