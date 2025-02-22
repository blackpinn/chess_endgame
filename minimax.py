from position_evaluation import position_evaluation

def minimax(board, depth, alpha, beta, maximizing_player):
    # Ak sme dosiahli zadanu hlbku alebo je koniec hry(mat/pat), ohodnotime poziciu
    if depth == 0 or board.is_game_over():
        return position_evaluation(board, maximizing_player)


    if maximizing_player:
        max_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Orezavanie vetiev, ktore uz nemusime prehladavat pre max hraca
        return max_eval
    
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break # Orezvanie vetiev, ktore uz nemusime prehladavat pre min hraca
        return min_eval

def checkmate_in_three_possible(board):

    # Inicilaizacia konstanty CHECKMATE_VALUE
    CHECKMATE_VALUE = 10_000

    # Prehladavame do hlbky 6 kedze ide o 3 tahy(pol tahy) kazdeho hraca
    score = minimax(board, 6, -float('inf'), float('inf'), True)
    return score == CHECKMATE_VALUE