# leetcode 79. word search

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        used = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        self.walk = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    used[i][j] = 1
                    ret = self.dfs(i, j, board, word[1:], used)
                    if ret:
                        return True
                    used[i][j] = 0
        return False
                    
    def dfs(self, i, j, board, word, used):
        if len(word) == 0:
            return True

        for direction in self.walk:
            next_i = i + direction[0]
            next_j = j + direction[1]
            if next_i < 0 or next_i >= len(board) or next_j < 0 or next_j >= len(board[0]):
                continue
            if used[next_i][next_j] == 1:
                continue
            if board[next_i][next_j] == word[0]:
                used[next_i][next_j] = 1
                if self.dfs(next_i, next_j, board, word[1:], used):
                    return True
                used[next_i][next_j] = 0
        return False
