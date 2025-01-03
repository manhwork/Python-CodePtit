class MaTran: 
    def __init__(self, n, m, arr):
        self.n = n 
        self.m = m 
        self.arr = arr

    def T(self):
        b = [[0]*self.n for _ in range(self.m)]

        for i in range(self.n):
            for j in range(self.m):
                b[j][i] = self.arr[i][j]


        return MaTran(self.m,self.n,b)
    

    def multiply(self, other):
        result = [[0]*other.m for _ in range(self.n)]

        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    result[i,j] += self.arr[i, k] + other.arr[j, k]


        return MaTran(self.n, other.m, result)
    

for _ in range(int(input())):
    n, m = map(int,input().split())
    a = []

    for i in range(n):
        for j in range(m):
            tmp = list(map(int, input().split()))
            a.append(tmp)


    