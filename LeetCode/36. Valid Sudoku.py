class Solution(object):
    def isValidSudoku(self, board):
        transpose = [list(i) for i in zip(*board)]
        i = 0;j = 0
        rows_count = {}
        col_count = {}
        small_board1 = {}
        small_board2 = {}
        small_board3 = {}
        while True:
            if i in (3, 6, 9) and j == 0:
                if sum(small_board1.values()) != list(small_board1.values()).count(1):
                    return False
                small_board1 = {}
                if sum(small_board2.values()) != list(small_board2.values()).count(1):
                    return False
                small_board2 = {}
                if sum(small_board3.values()) != list(small_board3.values()).count(1):
                    return False
                small_board3 = {}
            if i == 9:
                break
            if board[i][j] != '.':
                rows_count[board[i][j]] = rows_count.get(board[i][j], 0) + 1
            if transpose[i][j] != '.':
                col_count[transpose[i][j]] = col_count.get(transpose[i][j], 0) + 1
            if j < 3:
                if board[i][j] != '.':
                    small_board1[board[i][j]] = small_board1.get(board[i][j], 0) + 1
            elif j < 6:
                if board[i][j] != '.':
                    small_board2[board[i][j]] = small_board2.get(board[i][j], 0) + 1
            elif j < 9:
                if board[i][j] != '.':
                    small_board3[board[i][j]] = small_board3.get(board[i][j], 0) + 1
            j += 1
            if j == 9:
                if sum(rows_count.values()) != list(rows_count.values()).count(1):
                    return False
                rows_count = {}
                if sum(col_count.values()) != list(col_count.values()).count(1):
                    return False
                col_count = {}
                j = 0
                i += 1
        return True


