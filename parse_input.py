""" 
Tento modul sluzi na parsovanie FEN formatu, pouzivame kniznicu chess, vytvorime funkciu ktora bude vraciat objekt board, 
pomocou ktoreho uz vieme riesit samostatnu logiku. 
"""

import chess

class FENParser:

    def __init__(self, fen_format):
        self.fen_format = fen_format

    def fen_to_board(self):

        # kontrolujeme ci uzivatel na vstupe pouzil validny FEN format, ak ano, vratime objekt board
        try:
            board = chess.Board(self.fen_format)
            return board
        except ValueError as error:
            print("Zadany nespravny format, pozadovany format na vstupe je FEN.", error)
            return None

