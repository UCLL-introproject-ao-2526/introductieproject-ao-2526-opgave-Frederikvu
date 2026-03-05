**Logboek Project Blackjack (Pygame)**



**Introductie**

Dit logboek documenteert mijn volledige ontwikkelingsproces van het Blackjack‑project in Pygame. Het bevat niet alleen een chronologische weergave van wat ik gedaan heb, 

maar ook mijn reflecties, denkproces, fouten, oplossingen en keuzes. Het doel van dit logboek is om inzicht te krijgen in mijn manier van werken, 

mijn groei als programmeur, en de manier waarop ik problemen analyseer en oplos.



Zoals de cursus vraagt, probeer ik niet enkel te beschrijven wat ik gedaan heb, maar vooral waarom ik bepaalde beslissingen nam, hoe ik problemen onderzocht, en wat ik hieruit geleerd heb.



**## 27 Februari 2000 ##**

Ik ben gestart met het Blackjack‑project. Het opzetten van de omgeving verliep niet zoals verwacht: Pygame werkte niet. Ik dacht eerst dat ik iets verkeerd geïnstalleerd had, 

maar uiteindelijk bleek mijn Python‑versie te nieuw te zijn.

Het oplossen was eenvoudig eens ik wist waar ik moest zoeken: Python downgraden en de interpreter in VS Code aanpassen. 

Dit was een goede reminder dat compatibiliteit belangrijker is dan “de nieuwste versie hebben”.





**## 27 Februari 2100 ##**

Tijdens het volgen van de tutorial kreeg ik een foutmelding door een typfout (: in plaats van =). Het zoeken duurde langer dan het fixen. 

Dit bevestigt opnieuw dat kleine details grote gevolgen kunnen hebben.





**## 27 Februari 2130 ##**

De knoppen “HIT ME” en “STAND” stonden op dezelfde positie. Na het opnieuw bekijken van de tutorial vond ik de fout in de coördinaten. 

Het was een kleine correctie, maar het toont hoe belangrijk visuele controle is.





**##  28 Februari 0950 ##**

De kaarten lagen allemaal op elkaar. Ik dacht eerst dat de logica fout zat, maar uiteindelijk bleek ik een 1 te hebben geschreven in plaats van i. 

Een klassiek voorbeeld van hoe één karakter het hele beeld kan verstoren.





**##  28 Februari 1045 ##**

De tutorial ging vlot en zonder problemen. Het gaf me vertrouwen dat ik de basis van Pygame steeds beter begin te begrijpen.





**## 28 Februari 1300–1345 ##**

Deze sessie verliep zonder fouten. Ik kon de tutorial rustig volgen en voelde dat ik meer grip kreeg op de structuur van het spel.





**## 28 Februari 1655 ##**

Bij het klikken op “HIT” sloot het spel af. Ik dacht eerst aan een fout in de event‑loop, maar uiteindelijk bleek het een typfout in een variabele. 

Het zoeken duurde langer dan het fixen, maar ik word steeds systematischer in mijn aanpak.





**## 28 Februari 1720 ##**

Ik dacht dat er code ontbrak in de tutorial, maar na terugspoelen bleek alles toch te kloppen. 

Dit was een goede reminder om niet te snel conclusies te trekken.





**## 28 Februari 1745 ##**

Een foutmelding over indentatie. Twee regels stonden niet ingesprongen. 

Python blijft streng, maar het dwingt me wel om netter te werken.





**## 28 Februari 1800 ##**

Bij het klikken op “STAND” crashte het spel. De foutmelding wees naar een verkeerd gespelde variabele. 

De terminal hielp me snel naar de juiste plaats. Ik begin steeds meer te vertrouwen op foutmeldingen als hulpmiddel.





**## 28 Februari 1815 ##**

De tutorial is afgerond en het spel werkt volledig. Het voelt goed om een werkend spel te hebben én alle fouten zelf opgelost te hebben.





**## 01 Maart 1330 ##**

Ik heb filmpjes bekeken over Pygame‑game‑design. Dit gaf me inspiratie om mijn spel visueel aantrekkelijker te maken. 

Ik merkte dat ik niet enkel wil dat het werkt, maar dat het er ook goed uitziet.





**## 02 Maart 1830 ##**

Ik ben begonnen met een grote visuele update:

* nieuwe achterkant voor de dealerkaart
* realistischere speelkaarten
* achtergrondafbeelding
* geluidseffecten



Het was leuk om hiermee bezig te zijn, maar ook uitdagend. Vooral de geluiden bleven in een loop afspelen. Na wat experimenteren heb ik dat opgelost. 

Ik merk dat ik steeds meer plezier haal uit het verfijnen van de gebruikerservaring.





**## 03 Maart 1800 ##**

* Ik wilde het spel uitbreiden met:
* een startscherm
* dynamische schermgrootte
* betere score‑weergave
* mooiere knoppen
* aangepaste win‑berichten
* een nieuwe kaart: de (F)RedJoker



Ik begin steeds meer te denken als een game‑designer: niet alleen “werkt het?”, maar ook “voelt het goed aan?”.





**## 03 Maart 1815 ##**

Het startscherm is vernieuwd met een afbeelding en een mooie startknop. Het spel krijgt steeds meer een eigen identiteit.

&nbsp;



**## 03 Maart 1900 ##**

Mijn laptopscherm was te klein voor het spel. Dat frustreerde me. Ik heb de code aangepast zodat het spel zich automatisch aanpast aan de schermgrootte en afsluiten via Escape mogelijk is. 

Kleine verbeteringen, maar ze maken het spel veel aangenamer.





**## 03 Maart 2000 ##**

De scoreknoppen kregen een zwart‑goud thema. De positie moest ik bijsturen om overlapping te vermijden. 

Ook de dealer heet nu “Fred”, wat het spel persoonlijker maakt.





**## 03 Maart 2045 ##**

De overige knoppen heb ik in dezelfde stijl gebracht. Dit was lastiger dan verwacht, maar na veel itereren ziet het er professioneel uit.





**## 03 Maart 2150 ##**

De win/lose/draw‑berichten zijn aangepast naar het nieuwe thema. “Dealer Wins” werd “Fred Wins!”. 

Het zoeken naar de juiste positie kostte tijd, maar het resultaat is het waard.





**## 03 Maart 2250 ##**

De (F)RedJoker is toegevoegd. Als deze kaart valt, wint Fred automatisch. Ik heb de kaart via AI laten ontwerpen en een geluid toegevoegd. 

Het geeft het spel een unieke twist.





**## 04 Maart 1900 ##**

Ik heb de code opgesplitst in onderdelen en voorzien van commentaar. Het geheel is nu veel overzichtelijker. 

Ik merk dat ik dit soort structuur steeds belangrijker begin te vinden.





**## 05 Maart 1800 ##**

Ik heb een help‑knop toegevoegd die een handleiding toont. Het was even zoeken naar de juiste lettergrootte en positie, maar het werkt goed. 

Het spel begint echt aan te voelen als een compleet project.





**## Slotwoord ##**

Dit project heeft me veel geleerd, zowel technisch als procesmatig. Ik heb ervaren hoe belangrijk het is om systematisch te debuggen, om niet te snel conclusies te trekken, en om creativiteit te combineren met structuur.

Wat begon als een eenvoudige tutorial groeide uit tot een persoonlijk project waarin ik mijn eigen stijl, ideeën en oplossingen kon verwerken. Ik heb fouten gemaakt, oplossingen gezocht, nieuwe dingen geprobeerd en vooral veel geleerd.

Dit logboek toont niet alleen mijn vooruitgang, maar ook mijn groei in zelfvertrouwen en zelfstandigheid als programmeur.





