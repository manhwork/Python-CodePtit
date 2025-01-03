class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size + 1))  # Mảng cha
        self.rank = [1] * (size + 1)          # Mảng cấp độ

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Nén đường đi
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Kết hợp theo cấp độ
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    Q = int(data[0])
    uf = UnionFind(100000)
    results = []
    
    for i in range(1, Q + 1):
        X, Y, Z = map(int, data[i].split())
        if Z == 1:
            # Mở van giữa X và Y
            uf.union(X, Y)
        elif Z == 2:
            # Kiểm tra xem X và Y có cùng nhóm không
            if uf.find(X) == uf.find(Y):
                results.append(1)
            else:
                results.append(0)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
# 9
# 1 2 2
# 1 2 1
# 3 7 2
# 2 3 1
# 1 3 2
# 2 4 2
# 1 4 1
# 3 4 2
# 1 7 2