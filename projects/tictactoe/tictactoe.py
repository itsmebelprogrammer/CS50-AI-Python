"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    
    for row in board:
        for cell in row:
            if cell == X:
                x += 1
            elif cell == O:
                o += 1
            
    if x > o:
        return O
 
    return X          
             
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board[0])): 
            if board[i][j] == EMPTY:
                actions.add((i, j))
                
    return actions 
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if action is None or new_board[action[0]][action[1]] is not None:
        raise Exception("Invalid move.")
    
  
    p = player(board)
    new_board[action[0]][action[1]] = p
        
    return new_board
    
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY: 
            return board[0][j]    
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
            return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
 
 
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    if len(actions(board)) == 0:
        return True


    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)== X:
        return 1
    if winner(board)== O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        if terminal(board):
            return (utility(board), None)
        move = None
        v = -math.inf
        for action in actions(board):
             val = max(v, min_value(result(board, action))[0])
             if val > v:
                v, move = val, action
        return ((v, move))

    def min_value(board):
         if terminal(board):
             return (utility(board), None)
         move = None
         v = math.inf
         for action in actions(board):
             val = min(v, max_value(result(board, action))[0])
             if val < v:
                v, move = val, action
         return ((v, move))
         
    if player(board) == X:
        return(max_value(board)[1])
    else:
        return(min_value(board)[1])  
