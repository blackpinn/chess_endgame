"""
Tento modul obsahuje testovacie data zamerane na rozne typy koncoviek, ktore mozu nastat podla specifikacie.
"""

import unittest
import chess
from minimax import checkmate_in_three_possible

class TestPositions(unittest.TestCase):

    def test_simple_position_checkmate(self):
        # Jednoducha pozicia kedy je cierny kral na okraji sachovnice, biely hrac ma iba damu a je mozne vynutit mat do troch tahov
        fen = "7k/8/4K1Q1/8/8/8/8/8 w - - 0 1"
        board = chess.Board(fen)
        self.assertTrue(checkmate_in_three_possible(board), "Jednoducha koncovka s damou")
    
    def test_rook_checkmate(self):
        # Jednoducha pozicia kedy je cierny kral na okraji sachovnice, biely hrac ma iba vezu a je mozne vynutit mat do troch tahov
        fen = "1k6/6R1/3K4/8/8/8/8/8 w - - 0 1"
        board = chess.Board(fen)
        self.assertTrue(checkmate_in_three_possible(board), "Jednoducha koncovka s vezou")
    
    def test_bishop_knight_checkmate(self):
        # Zlozitejsia pozicia kedy ma biely hrac vynuteny mat do troch tahov, no len za pouziti kona a strelca
        fen = "k7/3B4/1K6/1N6/8/8/8/8 w - - 0 1"
        board = chess.Board(fen)
        self.assertTrue(checkmate_in_three_possible(board), "Zlozitejsia koncovka strelec,kon")
    
    def test_advanced_mate(self):
        # Zlozita pozicia kedy sa cierny kral nenachadza na okraji sachovnice ale v strede a biely hrac ma dostupnych viacero roznych figur(dama,veza,kon) daleko od seba
        fen = "7N/8/8/4k3/B7/2K5/2Q3R1/8 w - - 0 1"
        board = chess.Board(fen)
        self.assertTrue(checkmate_in_three_possible(board), "Zlozita koncovka kral v strede, rozne figury")

    def test_input_checkmate(self):
        # Pozicia kedy vynuteny mat moze nastat do menej ako troch tahov
        fen = "7k/5Q2/6K1/8/8/8/8/8 w - - 0 1"
        board = chess.Board(fen)
        self.assertTrue(checkmate_in_three_possible(board), "Pozicia v ktorej je mozny vynuteny mat do menej ako troch tahov")
    
    def test_checkmate_not_possible_in_three(self):
        # Pozicia kedy sa mat do troch tahov vynutit neda
        fen = "7k/8/8/3K4/8/5Q2/8/8 w - - 0 1"
        board = chess.Board(fen)
        self.assertFalse(checkmate_in_three_possible(board), "Pozicia v ktorej sa vynutit mat do troch tahov neda")

if __name__ == '__main__':
    unittest.main()