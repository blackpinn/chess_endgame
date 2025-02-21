def minimax(board, depth, alpha, beta, maximizing_player):
    # Ak sme dosiahli zadanu hlbku alebo je koniec hry(mat/pat), ohodnotime poziciu
    if depth == 0 or board.is_game_over():
        if board.is_checkmate():
            # Ak nastal mat, vratime vysoku hodnotu
            # V pripade ze nastal mat a na tahu je opacna farba aku sme zadali na vstupe, znamena to, ze zadana farba na vstupe(hrac ktory tahal ako prvy) ma vynutenu vyhru
            # V opacnom pripade ma vynutenu vyhru opacna farba ako je zadana na vstupe
            return 10000 if board.turn != maximizing_player else -10000
        return 0  # Ohodnotenie pre ostatne pripady ked mat nenastal

    if maximizing_player:
        max_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, maximizing_player)
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
            eval = minimax(board, depth - 1, alpha, beta, maximizing_player)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break # Orezvanie vetiev, ktore uz nemusime prehladavat pre min hraca
        return min_eval

def mate_in_three_possible(board):

    maximizing_player = board.turn # Inicializujeme max hraca, teda hraca ktory je v nasej pozicii prvy na tahu
    # Prehladavame do hlbky 6 kedze ide o 3 tahy(pol tahy) kazdeho hraca
    score = minimax(board, 6, -float('inf'), float('inf'), maximizing_player)
    
    return score == 10000