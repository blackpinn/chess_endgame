"""
Tento modul obsahuje testy, ktore sluzia na spravne zachytenie nekorektncyh vstupov: fen formatu a pozicii/koncoviek, ktore nesplnaju zadanu specifikaciu 
"""

import unittest
import chess
from check_board import is_white_first_to_move, opponent_only_black_king, check_white
from parse_input import FENParser

class TestValidInput(unittest.TestCase):

    def test_invalid_fen_detection(self):
        # Testovanie nekorektneho fen formatu
        fen = "7k\8\8\3K4\8\5Q2\8\8 w @ - 0 1"
        fen = FENParser(fen)
        self.assertFalse(FENParser.fen_to_board(fen), "Testovanie nekorektneho fen formatu")
    
    def test_black_missing_king(self):
        # Testovanie toho ci je v pozicii cierny kral
        fen = "6q1/8/3Q4/5K2/8/8/8/8 w - - 0 1"
        board = chess.Board(fen)
        res, output_message = opponent_only_black_king(board)
        self.assertFalse(res, "Testovanie chybajuceho cierneho krala")
    
    def test_black_having_other_pieces(self):
        # Testovanie ci cierny nema dostupne zakazane figurky
        fen = "8/8/3Q4/5K2/1n6/4k3/6b1/8 w - - 0 1"
        board = chess.Board(fen)
        res, output_message = opponent_only_black_king(board)
        self.assertFalse(res, "Testovanie nedovolenych figurok cierneho")
    
    def test_missing_white_king(self):
        # Testovanie ci ma v pozicii biely potrebneho krala
        fen = "8/8/3Q4/8/8/2k3R1/8/8 w - - 0 1"
        board = chess.Board(fen)
        res, output = check_white(board)
        self.assertFalse(res, "Testovanie chybajuceho bieleho krala")
    
    def test_white_to_move(self):
        # Testovanie ci je v pozicii prvy na tahu biely
        fen = "8/2K5/8/2Q5/k7/8/8/8 b - - 0 1"
        board = chess.Board(fen)
        res, output = is_white_first_to_move(board)
        self.assertFalse(res, "Testovanie pozicie kedy biely nieje prvy na tahu")

    def test_white_not_having_other_pieces(self):
        # Testovanie ci ma biely aj ine figurky okrem krala ci teda ide o validnu koncovku
        fen = "8/3K4/8/8/k7/8/8/8 w - - 0 1"
        board = chess.Board(fen)
        res, output_message = check_white(board)
        self.assertFalse(res, "Testovanie chybajucich potrebnych figurok bieleho")

if __name__ == '__main__':
    unittest.main()