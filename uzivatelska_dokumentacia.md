# Chess endgame program - uzivatelska dokumentacia

## Hlavny prehlad
- Program vie pre nizsie specifikovanu koncovku, urcit ci je mozne vynutit mat do troch tahov vratane, bielym hracom.

### Specifikacia koncovky
- Koncovka je pre ucely tohto programu specifikovana nasledovne:
- V zadanej pozicii vzdy zistujeme moznost matu pre hraca s bielymi figrukami, preto musi byt vzdy ako prvy na tahu biely hrac.
- Zrejme musia mat v zadanej pozicii obaja hraci dostupnych kralov.
- Biely hrac musi mat mimo krala dostupnu aspon jednu dalsiu figurku.
- Cierny hrac nesmie mat mimo krala dostupnu ziadnu dalsiu figurku.

## Instalacia a spustenie
- Je potrebne mat nainstalovany git,python a napriklad pomocou terminalu spustit nasledujuci prikaz:
```$ git clone https://github.com/blackpinn/chess_endgame```
- Potrebna je takisto instalacia kniznice chess pomocou ```pip instal chess```
- Tymto sposobom mate vsetky potrebne subory, mozete si ich otvorit v nejakom IDE napriklad VS Code, pre spustenie programu je potrebne spustit program ```main.py``` co je teda mozne pomocou nejakeho IDE alebo po prikaze git clone v terminali prejst do vytvoreneho repozitara pomocou ``` $ cd chess_endgame``` a nasledne spustit hlavny subor pomocou ```$ python main.py```

## Uzivatelske rozhranie
- Cele uzivatelske rozhranie je v textovom formate
### Zadavanie vstupu
- Na vstupe je potrebne zadat v jednom riadku FEN format danej pozicii kedy teda ide o koncovku ktora je specifikovana vyssie v ```Specifikacia koncovky``` nizsie je uvedene co to je FEN format co obsahuje a ako ho ziskat. Pred zadanim vstupu je uzivatelovi strucne uvdene fungovanie programu a specifikacia koncovky.
### Forma vystupu
- Ak je validny FEN a pozicia splna specifikaciu koncovky dostanete na vystupe informaciu o tom ci je mozne vynutit mat do troch tahov bielym hracom alebo nie, v opacnom pripade dostanete hlasenie popisujuce konkretny bod nesplnujuci specifikaciu koncovky alebo info o tom, ze ste zadali nespravny FEN format.

## FEN Format a priklad pouzitia
- FEN je standardizovany textovy format, ktory sa pouziva na zaznamenavanie stavu sachovej partie. Umoznuje jednoducho a kompaktne popisat akutalnu poziciu na sachovnici.
- FEN zapis sa sklada zo siestich casti, pricom jednotlive casti su oddelen medzerami.
- Prva cast: popisuje poziciu figur zlava do prava zacinajuc 8.radom az po 1.rad kazdy rad je oddeleny znakom: /
- cierne figurky su znacene malymi pismenami, biele figurky velkymi: r=cierna veza(rook), n=cierny jazdec(black knight) atd..
- Druha cast: popisuje aktivnu stranu: w - na tahu je biely hrac, b - na tahu je cierny hrac
- Tretia cast: popisuje moznost rosady: K - biela mala rosada, Q - biela velka rosada, rovnako pre cierneho s malymi pismenami
- Cielove policko pre en passant: Bud je uvedene policko kde je mozne vykonat en passant alebo en passant neni mozny ak je tam znak: -
- Piata cast: Udava polovicny pocet tahov teda pocet tahov od kedy obaja hraci naposledy posunuli pesiaka alebo doslo k vyhodeni nejakej figury
pouziva sa na detekovanie remizy
- Siesta cast: Udava celkovy pocet tahov, zvysuje sa vzdy po tahu cierneho

- Tu je priklad: ```rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1```

- Validnu poziciu pre tento program je teda mozne ziskat manualne pomocou tohto popisu a specifikacie koncovky vyssie.
- Dalsia moznost je pouzit nejaky sachovy program ako ChessBase, lichess.org, chess.com alebo samostatne sachove enginy.
- Sem uvediem priklad: [chess.com/analysis_board](https://www.chess.com/analysis?tab=analysis)
- Koncovku si mozete vytvorit kliknutim na ikonu ```+ Set Up Position```, nasledne pomocou baru ktory sa nachadaza pod ikonami figurok nastavit ```White to move```, vedla tohto baru kliknut na ikonku kosu, cim si poziciu vymazete, naseldne vybratim figurky a presunutim na pozadovane policko zostrojit pozadovanu koncovku splnujucu specifikaciu.

## Overenie spravneho fungovania
- V repozitari ktory si stiahnete su zahrnute aj dva unittest skripty obsahujuce testovacie data. Mozete si takto overit ze sa instalaciou nic nepokazilo a program funguje ako ma. Prvy unittest sluzi na otestovanie hlavnej logiky(pozicie splnujuce specifikaciu a format) pre rozne pripady, ktore mozu nastat(Obsiahnute su len tie najhlavnejsie). Druhy unittest sluzi na otestovanie zachytavania nie korektneho vstupu a pozicie nesplnujucu specifikaciu.
- Staci prejst do korenoveho adresara kde boli stiahnute vsetky subory otvorit terminal a nasledne spustit: 
pre prvy test: ```$ python endgame_position_tests.py``` 
pre druhy test: ```$ python valid_input_positiosn_tests.py```

```* Ikonku $ pouzivam len na rozlisenie ze ide o nejaky prikazovy riadok/terminal```