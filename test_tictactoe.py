import tictactoe as ttt
import copy
import math
board = ttt.initial_state()

from tictactoe import  EMPTY, X, O

colBrd = [[EMPTY, X, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, X, EMPTY]]
rowBrd = [[EMPTY, EMPTY, EMPTY],
            [O, O, O],
            [EMPTY, EMPTY, EMPTY]]
diagBrd = [[EMPTY, EMPTY, X],
            [EMPTY, X, EMPTY],
            [X, EMPTY, EMPTY]]
fullbrd = [[O, O, X],
            [X, X, O],
            [O, O, X]]

# player = ttt.player(ttt.initial_state())
# print(player, "player Is")
plyBrd = ttt.initial_state()
# plyBrd[0][0]=X
# print(ttt.player(plyBrd), "player Is")
# plyBrd[0][1]=O
# print(ttt.player(plyBrd), "player Is")
plyBrd1 =ttt.result(plyBrd,(0,2))
print("board:",plyBrd1)
print(ttt.player(plyBrd1), "player Is after result ")
print("actions:", ttt.actions(plyBrd1))
winner = ttt.winner(colBrd)
# print(winner," is the winner")
# winner = ttt.winner(rowBrd)
# print(winner," is the winner")
# winner = ttt.winner(diagBrd)
# print(winner," is the winner")
# winner = ttt.winner(fullbrd)
# print(winner," is the winner")

# terminal = ttt.terminal(colBrd)
# print(terminal," is the terminal")
# terminal = ttt.terminal(rowBrd)
# print(terminal," is the terminal")
# terminal = ttt.terminal(diagBrd)
# print(terminal," is the terminal")
# terminal = ttt.terminal(fullbrd)
# print(terminal," is the terminal")