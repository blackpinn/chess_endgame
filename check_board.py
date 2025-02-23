import chess

"""
V tomto module je vytvorena funkcia, ktora bude kontrolovat spravnost zadanej pozicie na vstupe podla specifikiacii ktore su uvedene v hlavicke main.py, 
na zaklade toho bude davat spatneinfo na vystup
"""

# Funkcia sluzi na overenie ze v zadanej pozicii je na tahu prvy hrac biely ako je uvedene v specifikacii
def is_white_first_to_move(board):
    
    output_message = ""

    if board.turn:
        return True, output_message
    else:
        output_message = "Pozicia nesplna specifikaciu, ako prvy na tahu nieje biely hrac."
        return False, output_message

# Funkcia sluzi na zistenie toho ci ma cierny hrac iba krala ako je vyzadovane v specifikacii
def opponent_only_black_king(board):

    output_message = ""
    black_king = False

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None and piece.color == chess.BLACK and piece.piece_type == chess.KING:
            black_king = True
        elif piece is not None and piece.color == chess.BLACK and piece.piece_type != chess.KING:
            output_message = "Hrac s ciernymi figurkami nesplna specifikaciu, ma k dispozicii inu figuru ako krala."
            return False, output_message
    if not black_king:
        output_message = "Hrac s ciernymi figurkami nesplna specifikaciu, nema k dispozicii krala."
        return False, output_message
    return True, output_message

def check_white(board):

    output_message = ""
    white_king = False
    other_piece = False

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None and piece.color == chess.WHITE and piece.piece_type == chess.KING:
            white_king = True
        elif piece is not None and piece.color == chess.WHITE and piece.piece_type != chess.KING:
            other_piece = True

    if not white_king:
        output_message = "Hrac s bielymi figurkami nesplna specifikaciu, nema k dispozicii krala."
        return False, output_message
    if not other_piece:
        output_message = "Hrac s bielymi figurkami nesplna specifikaciu, nema k dispozicii inu figurku ako krala."
        return False, output_message
    return True, output_message