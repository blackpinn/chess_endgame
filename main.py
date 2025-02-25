# Sachove koncovky (definicia koncovky nizsie) hlbka = 3 tahy
# Miroslav Pasztor, I.rocnik
# zimni semestr 2024/25
# Programovani I NPRG030	

from parse_input import FENParser
from minimax import checkmate_in_three_possible
from check_board import is_white_first_to_move, opponent_only_black_king, check_white

"""
Od uzivatela ziadame input teda korektny FEN format sachovej koncovky, ktora je definovana tak, ze cierny hrac ma k dispozicii
iba krala, dalej v takomto korektnom FEN formate musi byt ako prvy na tahu biely hrac, zaroven ma biely hrac mat krala a este aspon jednu figuru,
na vystup vraciame informaciu o tom, ci je mozne vynutit mat do troch tahov bielym hracom. Pomocou parse_input modulu kontrolujeme spravnosť FEN formatu a ziskavame objekt board,
s ktorym pracujeme dalej pomocou ostatnych modulov az dostavame vystup, informaciu o moznosti vynuteneho matu do troch tahov bielym hracom.
"""

if __name__ == '__main__':
    import unittest
    unittest.main()

    print("\n'''Tento program sluzi na vyhodnotenie moznosti vynuteneho matu do troch tahov bielym hracom v sachovej koncovke.'''\n")
    print("                  Vo FEN formate zadajte sachovu koncovku v ktorej je na tahu biely hrac.\n")
    print("                Za sachovu koncovku berieme poziciu v ktorej ma cierny hrac iba figuru krala.\n")
    print("                      Biely hrac musi mat dostupneho krala a este aspon jednu figuru.\n")
    print("---------------------------------------------------------------------------------------------------------------------\n")
    fen_str = FENParser(input("Zadaj platny FEN retazec podla poziadaviek uvedenych vyssie: "))

    board = fen_str.fen_to_board()

    condition_1, condition_1_message = is_white_first_to_move(board)
    condition_2, condition_2_message = opponent_only_black_king(board)
    condition_3, condition_3_message = check_white(board)

    # Kontrolujeme ci su splnene specifikacie zadanej pozicie na vstupe, ktora je uvedena v hlavicke tohto suboru
    if condition_1 and condition_2 and condition_3:
        if checkmate_in_three_possible(board):
            print("\nAk je pre zadanu poziciu prvy na tahu biely hrac, je mozne vynutit mat do troch tahov.\n")
        else:
            ("\nAk je pre zadanu poziciu prvy na tahu biely hrac, mat do troch tahov nie je mozne vynutit.\n")
    else:
        if not condition_1:
            print(f"\n{condition_1_message}\n")
        if not condition_2:
            print(f"\n{condition_2_message}\n")
        if not condition_3:
            print(f"\n{condition_3_message}\n")
