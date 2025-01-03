def ql(start, n, k, cur, index):
    if len(cur) == k:
        index.append(cur[:]) 
        return 
    
    for i in range(start, n + 1):
        cur.append(i)
        ql(i + 1, n, k, cur, index)
        cur.pop()

n, k = map(int,input().split())
a = list(map(int,input().split()))
index = []

ql(1,n,k,[],index)
print(index)

tong = []
for x in index : 
    tong.append(abs(a[x[0] - 1] - a[x[1] -1]))
print(tong)

