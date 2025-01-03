class MaTran:
    def __init__(self, n, m, mang):
        self.n = n 
        self.m = m 
        self.mang = mang

    def T(self):
        b = [[0]*self.n for _ in range(self.m)]
        
        for i in range(self.n) :
            for j in range(self.m) :
                b[j][i] = self.mang[i][j]

        return MaTran(self.m,self.n, b )
    

    def multiply(self, other):
        result = [[0]*other.m for _ in range(self.n)]

        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    result[i][j] += self.mang[i][k] * other.mang[k][ j]


        return MaTran(self.n, other.m, result)



for _ in range(int(input())):
    n, m = map(int,input().split())
    
    a = []
    
    for i in range(n):
        tmp = list(map(int,input().split()))
        a.append(tmp)

    mt1 = MaTran(n, m, a)

    mt2 = mt1.T()

    for row in mt1.multiply(mt2).mang:
        print(" ".join(map(str, row)))

"""
1
2  3
1  2  3
4  5  6
1
2  2
1  2
3  4
"""
