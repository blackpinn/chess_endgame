from parse_input import FENParser
from minimax import mate_in_three_possible


"""
Od uzivatela ziadame input, pomocou vytvorenej classy kontrolujeme spravnosť FEN formatu a ziskavame objekt board,
s ktorym pracujeme dalej.
"""

if __name__ == '__main__':
    fen_str = FENParser(input("Zadaj FEN retazec: "))
    board = fen_str.fen_to_board()
    print(board)
    if mate_in_three_possible(board):
        print("Mat do troch tahov je mozny.")
    else:
        print("Mat do troch tahov nie je mozny.")


