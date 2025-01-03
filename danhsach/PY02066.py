n = int(input())

a  = []

cnt = 0 

while cnt != n :
    tmp = list(map(int,input().split()))
    a.extend(tmp)
    cnt += len(tmp)

maxn = max(a) 

check = False

for i in range(1, maxn + 1):
    if i not in a : 
        print(i)
        check = True

if check == False: 
    print("Excellent!")


print(a)





"""
7
4 5 7 8 9
10 11
5
1 2 3
4
5
4
1 2 3 5
"""