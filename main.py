from parse_input import FENParser
import chess

"""
Od uzivatela ziadame input, pomocou vytvorenej classy kontrolujeme spravnosť FEN formatu a ziskavame objekt board,
s ktorym pracujeme dalej.
"""

fen_str = input("Zadaj FEN reťazec: ")
parser = FENParser(fen_str)
board = parser.fen_to_board()

print(board)