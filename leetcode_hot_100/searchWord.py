# hot100-lc 79. searchWord

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ret = False
        used_in_board = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    used_in_board[i][j] = True
                    ret = self.search(i, j, used_in_board, board, word[1:])
                    if ret:
                        return True
                    used_in_board[i][j] = False
        return False

    def search(self, i, j, used_in_board, board, word):
        if len(word) == 0:
            return True

        for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 上下左右
            next_i, next_j = i + move[0], j + move[1]
            if next_i < 0 or next_j < 0 or next_i >= len(used_in_board) or next_j >= len(used_in_board[0]):
                continue
            if used_in_board[next_i][next_j]:
                continue
            if board[next_i][next_j] == word[0]:
                used_in_board[next_i][next_j] = True
                ret = self.search(next_i, next_j, used_in_board, board, word[1:])
                if ret:
                    return True
                used_in_board[next_i][next_j] = False
        return False
