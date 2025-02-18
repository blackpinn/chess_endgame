import chess

"""
Tento modul sluzi na ohodnotenie aktualnej sachovej pozicie, na zaklade volnych policok, vzdialenosti damy, ci sa kral nachadza
na okraji sachovnice ci nenastal mat atd.. Podla tychto kriterii bude aktualnej pozicii pridelena hodnota.
"""

def position_evaluation(board):

    score = 0 # inicializacia ohodnotenia pre aktualnu poziciu

    # aktualna pozicia(policko) cierneho krala
    black_king_pos = board.king(chess.BLACK)

    # stlpec a riadok cierneho krala
    file = chess.square_file(black_king_pos)
    rank = chess.square_rank(black_king_pos)

    if file in [0,7] or rank in [0,7]:
        score += 3 # zvysenie ohodnotenia aktualnej pozicie
    
    temp_board = board.copy() # kopia aktualnej pozicie
    temp_board.turn = chess.BLACK # zaujimaju nas moznosti na tah cierneho krala

    black_moves = 0 # inicializacia poctu moznych tahov cierneho krala

    for move in temp_board.legal_moves:
        if move.from_square == black_king_pos: # filtrovanie tahov ktore vychadzaju len z policka na ktorom sa nachadza cierny kral
            black_moves += 1
    
    # Na zaklade moznych tahov zvysujeme hodnotu aktualnej pozicie
    if black_moves >= 5:
        score +=1 
    elif 3 <= black_moves <= 4:
        score += 3
    elif 0 < black_moves <= 2:
        score += 5

    # Kontrolujeme ci nastal mat alebo pat
    if not board.is_checkmate() and black_moves == 0:
        score = 100 # nastal pat
    elif black_moves == 0 and board.is_checkmate():
        score = 1000 # nastal mat

    return score