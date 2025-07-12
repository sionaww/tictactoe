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
    xcount = 0
    ocount = 0
    if terminal(board) is False:
        for row in board:
            for cell in row:
                if cell == X:
                    xcount += 1
                elif cell == O:
                    ocount += 1
        if xcount == ocount:
            return X
        elif xcount > ocount:
            return O
        else:
            return EMPTY
    return None
    

def actions(board):
    actions = []
    for row in range(3):
            for cell in range(3):
                if board[row][cell] == EMPTY:
                    actions.append((row, cell))
    return actions                
    
   


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board = copy.deepcopy(board)
    if action not in actions(board):
        raise ValueError("move not permissable")
    else:
        if player(board) is X:
            board[action[0]][action[1]] = X
        elif player(board) is O:
            board[action[0]][action[1]] = O
    return board
    
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] != EMPTY and board[0][0] == board[1][1] and board[1][1] == board[2][2] or board[0][2] != EMPTY and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[1][1] == X:
            return X
        elif board[1][1] == O:
            return O
   
    for row in range(3):
        if board[row][0]!= EMPTY and board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == X:
                return X
            else:
                return O
    for cell in range(3):
        if board[0][cell]!= EMPTY and board[0][cell] == board[1][cell] and board[1][cell] == board[2][cell]:
            if board[0][cell] == X:
                return X
            else:
                return O
    for row in range(3):
        for cell in range(3):
            if board[row][cell] == EMPTY:
                return None

    return None
            
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True
 
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    elif winner(board) is None and all(board[row][cell] != EMPTY for row in range(3) for cell in range(3)): 
        return 0 
    return None
       
       
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) is X:
        return (maxvalue(board)[1])
    else:
        return (minvalue(board)[1])            

def maxvalue(board):
    if terminal(board):
        return (utility(board), None)
    current_valTuple = (float('-inf'), None)
    for action in actions(board):
        valTuple = minvalue(result(board, action))
        if  current_valTuple[0] < valTuple[0]:
            current_valTuple = (valTuple[0], action)
    return current_valTuple 
   
def minvalue(board):
    if terminal(board):
        return (utility(board), None)

    current_valTuple = (float('inf'), None)
    for action in actions(board):
        valTuple = maxvalue(result(board, action))
        if  current_valTuple[0] > valTuple[0]:
            current_valTuple = (valTuple[0], action)
    return current_valTuple 
   
# def minvalue(board):
#         min_vals = []
#         v = float('inf')
#         vAction = None
#         for action in actions(board):
#             current_val = min(maxvalue(result(board, action)[0]))
#             if v > current_val:
#                 v = current_val
#         best_action = (v, action)
#         return best_action 
            
  
   

    
