def ql( s, n, a, b, c):
    if (len(s) == n and a >0 and a <= b and b <= c):
        print(s)
    if (len(s) < n):
        ql(s + 'A', n, a + 1, b, c)
        ql(s + 'B', n, a , b+1, c)
        ql(s + 'C', n, a , b, c+1)


n = int(input())
for i in range(3,n+1):
    ql("",i,0,0,0)
