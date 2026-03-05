**LOGBOEK SCRATCH VERSIE PYGAME BLACKJACK**



**27/02/2026 20:00**

* **start sessie 1**
* start project Blackjack
* nieuwe map aangemaakt met de naam "project" in de introductieproject map
* deze map geopend in VSC en een nieuw bestand aangemaakt:pygame\_blackjack.py



**27/02/2026 20:10**

* start met het bekijken van de video
* de eerste lijnen code geschreven gelijktijdig met de video



**27/02/2026 20:25**

* PROBLEEM: 	in de video werd een print gedraaid via run, daar kreeg ik een error:ModuleNotFoundError: No module named 'pygame'
* OPLOSSING: 	na wat zoekwerk en met de hulp van CoPilot bleek dat de Python versie die actief was "te recent" te zijn (3.14.2) om Pygame te gebruiken.

&nbsp;		via CoPilot heb ik Python kunnen omzetten naar 3.12.10

&nbsp;		in VSC code heb ik dit ook kunnen omzetten via ctrl+shift+P -> Python: Select Interpreter en dan 3.12.10 gekozen

&nbsp;		opnieuw de run gedaan en toen lukte het wel



**27/2/2026 21:00**

* PROBLEEM:	error bij run: na wat zoek werk was het een typfout (: ipv = getypt).
* OPLOSSING: 	na wat zoek werk was het een typfout (: ipv = getypt), dit heb ik aangepast en de error is opgelost



**27/2/2026 21:30**

* PROBEEM: 	layout in blackjack spel was niet goed: "HIT ME" en "STAND" staan op dezelfde plaats
* OPLOSSING:	tutorial nog eens goed bekeken en oorzaak gevonden :screen.blit(stand\_text, (35, 735)) -> dit moet 355,735 zijn (hit\_text is al op plaats 35, 735)

&nbsp;		dit gecorrigeerd en het is terug in orde

* ondertussen zijn we 1u30min bezig met het project en hebben we al een mooi zwart scherm met daarin 2 knoppen (hit me en stand)



**27/2/2026 22:30**

* einde sessie: tutorial tot aan minuut 31:47



**totaal tijd sessie 1: 1u30min**

**aantal errors/problemen succesvol opgelost:3**







**28/2/2026 09:30**

* start sessie 2



**28/2/2026 09:50**

* PROBLEEM: in de tutorial zijn de kaarten mooi zichtbaar met wat overlap, bij mij liggen ze op elkaar
* OPLOSSING: oorzaak gevonden, in de code ergens 1 geschreven in plaats van i -> aangepast en probleem opgelost



**28/2/2026 10:45**

* einde sessie: tutorial tot aan minuut 38:36



**totaal tijd sessie 2: 1u15min**

**aantal errors/problemen succesvol opgelost:1**







**28/2/2026 13:00**

* start sessie 3



**28/2/2026 13:45**

einde sessie: tutorial tot aan minuut 56:18 -> geen issues gehad, alles vlot kunnen volgen



**totaal tijd sessie 3: 45min**

**aantal errors/problemen succesvol opgelost:0**







**28/2/2026 16:45**

* start sessie 4



**28/2/2026 16:55**

* PROBLEEM: 	als ik op 'HIT' klik sluit het spel af
* OORZAAK:	op regel 155 stond een fout (game\_deck\_deck ipv game\_deck)
* OPLOSSING:	dit gecorrigeerd en het is in orde.





**28/2/2026 17:20**

* PROBLEEM :	even onduidelijkheid in filmpje na break op 1u09min
* OORZAAK: 	er lijken een paar regels bij in de code te staan op het filmje die ik niet eerder gezien heb
* OPLOSSING:	filmpje even terug gespoeld en mijn code goed vergeleken met filpmje, lijkt toch in orde te zijn



**28/2/2026 17:45**

* PROBLEEM:	foutmelding : expected an indented block after 'if' statement on line 218
* OORZAAK	de 2 volgende lijnen waren niet ingesprongen naar rechts, ze stonden gewoon onder if
* OPLOSSING:	de 2 lijnen naar rechts ingesprongen



**28/2/2026 18:00**

* PROBLEEM:	bij test spelletje sluit het spel af wanneer ik op stand klik
* OORZAAK:	op lijn 134 stond 'de' in plaats van 'dealer\_score' (gevonden via melding in Terminal)
* OPLOSSING:	dit gecorrigeerd naar dealer \_score



**28/2/2026 18:15**

* einde tutorial
* spelletje diverse keren getest en alles lijkt prima te werken



**28/2/2026 18:30**

* einde sessie



**totaal tijd sessie 4: 1u45min**

**aantal errors/problemen succesvol opgelost: 4**



**samenvatting:**



* **totaal tijd volgen tutorial en maken spelletje Blackjack in VSC: 5u15min**
* **aantal errors/problemen: 8**
* **duidelijkheid instructies video: zeer goed, 1 van de beste tutorials die al gevolgd heb**



















































