class Solution:
    def __init__(self, matrix):
        self.matrix = matrix
        self.count = sum(sum(self.matrix[i]) for i in range(len(matrix)))
        self.fatherMap = {}
        self.setNumMap = {}
        n = 0
        for arr in self.matrix:
            for ele in arr:
                self.fatherMap[n] = n
                self.setNumMap[n] = 1
                n += 1
    
    def findFather(self, node):
        father = self.fatherMap[node]
        if node != father:
            father = self.findFather(father)
        self.fatherMap[node] = father    
        return father

    def union(self, p, q):
        pFather = self.findFather(p)
        qFather = self.findFather(q)
        if pFather != qFather:
            pFather_nums = self.setNumMap[pFather]
            qFather_nums = self.setNumMap[qFather]
            if pFather_nums <= qFather_nums:
                self.fatherMap[pFather] = qFather
                self.setNumMap[qFather] = pFather_nums + qFather_nums
                self.setNumMap.pop(pFather)
            else:
                self.fatherMap[qFather] = pFather
                self.setNumMap[pFather] = pFather_nums + qFather_nums
                self.setNumMap.pop(qFather)
            self.count -= 1

    def num_islands(self):
        row, col = len(self.matrix), len(self.matrix[0])
        for i in range(row):
            for j in range(col):
                if self.matrix[i][j] == 0:
                    continue
                # current element is 1
                cur_idx = i * col + j
                if j+1 < col and self.matrix[i][j+1] == 1:
                    self.union(cur_idx, cur_idx+1)
                if i+1 < row and self.matrix[i+1][j] == 1:
                    self.union(cur_idx, cur_idx+col)
        return self.count

matrix = [[1,1,0,1,0,1], [1,1,0,0,0,1], [0,0,0,1,0,1], [1,1,1,0,0,0]]
solution = Solution(matrix)
count = solution.num_islands()
print(count)

"""
110101
110001
000101
111000
"""

    