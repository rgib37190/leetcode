class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for i in range(n)]
        all_choices = []
        def backtrack(board, row):
            # board : 選擇列表 row : 路徑
            # 終止條件
            if row == len(board):
                all_choices.append(["".join(i) for i in board])
            for col in range(len(board)):
                # 跳過不合法選擇
                if self.hasQueen(board, row, col):
                    continue
                board[row][col] = "Q"
                backtrack(board, row + 1)
                board[row][col] = "."
        backtrack(board, 0)
        return all_choices

    def hasQueen(self, board, row, col):
        for i in range(len(board)):
            # 檢查上下列有無皇后
            if board[i][col] == "Q":
                return True
        # 檢查右上
        temp_row = row - 1
        temp_col = col + 1
        while (temp_row >= 0) and (temp_col < len(board)):
            if board[temp_row][temp_col] == "Q":
                return True
            temp_row = temp_row - 1
            temp_col = temp_col + 1
        #檢查左上
        temp_row = row - 1
        temp_col = col - 1
        while (temp_row >= 0) and (temp_col >= 0):
            if board[temp_row][temp_col] == "Q":
                return True
            temp_row = temp_row - 1
            temp_col = temp_col - 1
        return False
