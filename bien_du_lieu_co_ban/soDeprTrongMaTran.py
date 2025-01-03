from math import *

n ,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

maxn = max([max(x) for x in a])
minn = min([min(x) for x in a])

sodep = maxn - minn
ok = False
lsodep = []

for i in range(n):
    for j in range(m):
        if a[i][j] == sodep :
            ok = True
            lsodep.append("Vi tri [{}][{}]".format(i,j))

if ok == True :
    print(sodep)
    print(*lsodep,sep='\n')
else :
    print("NOT FOUND")




# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 67 28 23
# 29 77 11 67
# 16 51 24 21
# 13 25 77 77