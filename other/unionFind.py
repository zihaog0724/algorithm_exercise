class UnionFind:
    def __init__(self, nodes):
        self.fatherMap = {}
        self.numMap = {}
        for node in nodes:
            self.fatherMap[node] = node # father of every node
            self.numMap[node] = 1 # num_elements of every set

    def findFather(self, node):
        '''
        recursion
        base case: node = father
        '''
        father = self.fatherMap[node]
        if node != father:
            father = self.findFather(father)
        self.fatherMap[node] = father
        return father 

    def is_same_set(self, p, q):
        return self.findFather(p) == self.findFather(q)

    def union(self, p, q):
        p_father = self.findFather(p)
        q_father = self.findFather(q)

        if p_father != q_father:
            p_father_num = self.numMap[p_father]
            q_father_num = self.numMap[q_father]
            if p_father_num <= q_father_num:
                self.fatherMap[p_father] = q_father
                self.numMap[q_father] = p_father_num + q_father_num
                self.numMap.pop(p_father)
            else:
                self.fatherMap[q_father] = p_father
                self.numMap[p_father] = p_father_num + q_father_num
                self.numMap.pop(q_father)

# Test
if __name__ == '__main__':
    nodes = ['soccer', 'ski', 'jogging', 'football', 'skating', 'marathon']
    uf = UnionFind(nodes)

    uf.union('soccer', 'football')
    uf.union('ski', 'skating')
    uf.union('marathon', 'jogging')
    uf.union('soccer', 'skating')
    uf.union('marathon', 'ski')

    print(uf.fatherMap)
    print(uf.numMap)

    print(uf.is_same_set('soccer', 'ski'))  # True
    print(uf.is_same_set('soccer', 'football'))  # False
    print(uf.is_same_set('skating', 'marathon'))  # False
    print(uf.is_same_set('jogging', 'ski'))  # True
    