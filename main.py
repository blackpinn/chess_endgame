from parse_input import FENParser
from minimax import checkmate_in_three_possible


"""
Od uzivatela ziadame input teda korektny FEN format sachovej koncovky, ktora je definovana tak, ze cierny hrac ma k dispozicii
iba krala, dalej v takomto korektnom FEN formate musi byt ako prvy na tahu biely hrac, na vystup vraciame informaciu o tom, ci je mozne
vynutit mat do troch tahov bielym hracom. Pomocou parse_input modulu kontrolujeme spravnosť FEN formatu a ziskavame objekt board,
s ktorym pracujeme dalej pomocou ostatnych modulov az dostavame vystup, informaciu o moznosti vynuteneho matu do troch tahov bielym hracom.
"""

if __name__ == '__main__':

    fen_str = FENParser(input("Zadaj platny FEN retazec podla poziadaviek uvedenych vyssie: "))
    board = fen_str.fen_to_board()

    if checkmate_in_three_possible(board):
        print("\nAk je pre zadanu poziciu prvy na tahu biely hrac, je mozne vynutit mat do troch tahov.\n")
    else:
        ("\nAk je pre zadanu poziciu prvy na tahu biely hrac, mat do troch tahov nie je mozne vynutit.\n")

# skontrolovat z parse_input ci je board validna.
# dopisat info o fungovani programu a ocakavanom vstupe do komentarov aj na vystup