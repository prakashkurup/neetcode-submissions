class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}
        self.count = 0

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
            self.count += 1

    def find(self, x):
        self.add(x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return False

        if self.size[x] < self.size[y]:
            x_root, y_root = x_root, y_root
        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]
        self.count -= 1

        return True
        

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind()

        for node in range(n):
            uf.add(node)

        for n1, n2 in edges:
            if not uf.union(n1, n2):
                return False
            
        return True if uf.count == 1 else False
        