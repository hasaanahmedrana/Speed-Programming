def validating(board):
    transpose = [list(i) for i in zip(*board)]
    i = 0;j = 0
    rows_count = {}
    col_count = {}
    small_board = {}
    for each in board:
        print(each)
    while True:
        if (i==2 and j==3) or (i==2 and j==6) or (i==5 and j==3)  or (i==5 and j==6) or (i==8 and j==3) or (i==8 and j==8) or i in (3,6,9)  :
            print(small_board)
            if len(small_board) != list(small_board.values()).count(1):
                print(1)
                return False
            small_board = {}
        if i == 9:
            break
        if board[i][j] != '.':
            rows_count[board[i][j]] = rows_count.get(board[i][j], 0) + 1
        if transpose[i][j] != '.':
            col_count[transpose[i][j]] = col_count.get(transpose[i][j], 0) + 1
        if j in [0, 3, 6] and i in [0, 3, 6]:
            if board[i][j] != '.':
                small_board[board[i][j]] = small_board.get(board[i][j], 0) + 1
            if board[i][j + 1] != '.':
                small_board[board[i][j + 1]] = small_board.get(board[i][j + 1], 0) + 1
            if board[i][j + 2] != '.':
                small_board[board[i][j + 2]] = small_board.get(board[i][j + 2], 0) + 1
        j += 1
        if j == 9:
            if 1 not in rows_count.values():
                print(2)
                return False
            rows_count = {}
            if 1 not in col_count.values():
                print(col_count)
                print(3)
                return False
            col_count = {}
            j = 0
            i += 1
    return True
print(validating([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))