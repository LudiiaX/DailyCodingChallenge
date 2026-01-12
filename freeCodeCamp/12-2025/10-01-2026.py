def verify_row(board):
    for i in board:
        if all(j == i[0] for j in i):
            return i[0] + " wins"

def verify_column(board):
    for i in range(len(board)):
        if all(j == board[0][i] for j in [board[0][i],board[1][i],board[2][i]]):
            return board[0][i] + " wins"

def verify_diag(board):
    diag = [[board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]]]
    for i in diag:
        if all(j == i[0] for j in i):
            return i[0] + " wins"

def tic_tac_toe(board):
    res = verify_diag(board)
    if res != None:
        return res
    res = verify_column(board)
    if res != None:
        return res
    res = verify_row(board)
    if res != None:
        return res
    
    
    return "Draw"


print(tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]))
print(tic_tac_toe([["X", "O", "X"], ["X", "O", "X"], ["O", "O", "X"]]))
print(tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]))
print(tic_tac_toe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]]))
print(tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]))
print(tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]))