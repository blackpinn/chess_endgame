import chess

"""
Tento modul sluzi na ohodnotenie aktualnej sachovej pozicie, na zaklade volnych policok na pohyb superovho krala, na zaklade toho ci sa kral nachadza
na okraji sachovnice, ci nenstal mat/path, ako daleko su od seba krali na sachovnici. Podla tychto kriterii a pre mat/path aj podla toho ci ide o max/min hraca bude aktualnej pozicii pridelena hodnota.
"""

# Funkcia zistujuca vzdialenost medzi kralmi
def kings_distance(board):

    # Ziskame pozicie oboch kralov
    white_king_square = board.king(chess.WHITE)
    black_king_square = board.king(chess.BLACK)

    # Potrebujeme zistit konkretny stlpec a riadok pozicii kralov
    white_file, white_rank = chess.square_file(white_king_square), chess.square_rank(white_king_square)
    black_file, black_rank = chess.square_file(black_king_square), chess.square_rank(black_king_square)

    # vratime vzdialenost kralov
    return max(abs(white_file-black_file), abs(white_rank-black_rank))

# Tato funkcia sluzi na lepsie sprehladnenie, kedze potrebujeme podla prehravajuceho krala vzdy zistit jeho poziciu a pocet legalnych tahov na urcenie hodnoty danej pozicie 
def get_loosing_king_info(board):

    # Inicializujeme prehravajuceho krala a zistime jeho policko
    king_to_checkmate = board.king(chess.BLACK)

    # Zistime pocet legalnych tahov a stlpec/riadok prehravajuceho hraca
    king_legal_moves = sum(1 for move in board.legal_moves if move.from_square == king_to_checkmate)
    file = chess.square_file(king_to_checkmate)
    rank = chess.square_rank(king_to_checkmate)

    return file,rank,king_legal_moves


def position_evaluation(board, maximizing_player):

    # Na ohodnotenie aktualnej pozicie potrebujeme zistit aktualne dolezite info o prehravajucom kralovi, jeho poziciu(stlpec,riadok) a pocet legalnych tahov
    king_to_checkmate_file, king_to_checkmate_rank, king_legal_moves = get_loosing_king_info(board) 

    # Inicializacia konstant pre hodnoty remizy, matu a dolezitych hodnot stlpcov a riadkov na sachovnici
    DRAW_VALUE = 1000
    CHECKMATE_VALUE = 10_000
    FIRST_FILE, LAST_FILE = 0,7
    FIRST_RANK, LAST_RANK = 0,7

    score = 0 # inicializacia ohodnotenia pre aktualnu poziciu

    if king_to_checkmate_file in (FIRST_FILE, LAST_FILE) or king_to_checkmate_rank in (FIRST_RANK, LAST_RANK):
        score +=  10 # zvysenie ohodnotenia aktualnej pozicie kedze sa kral nachadza na okraji sachovnice
    
    # Na zaklade poctu legalnych tahov zvysujeme hodnotu aktualnej pozicie
    if king_legal_moves <= 3:
        score += 50

    # Na zaklade vzdialenosti kralov zvysujeme hodnotu aktualnej pozicie
    if kings_distance(board) < 3:
        score += 50

    if board.is_checkmate():
        # Ak nastal mat, vratime vysoku hodnotu - predom danu konstantu CHEKCMATE_VALUE
        if maximizing_player:
            return -CHECKMATE_VALUE
        else:
            return CHECKMATE_VALUE
    elif board.is_game_over() and not board.is_checkmate():
        # Ak nastal pat, vratime vysoku hodnotu, no nizsiu nez pre mat - predom danu konstantu DRAW_VALUE
        score =  -DRAW_VALUE

    return score