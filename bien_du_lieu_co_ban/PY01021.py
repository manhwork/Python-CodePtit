def check(a, n):
    for i in range(n):
        for j in range(i, n):
            if a[i][j] != a[j][i]:
                return False
            
    return True

for _ in range(int(input())):
    n = int(input())
    a = []

    for i in range(n):
        tmp = list(map(int,input().split()))
        a.append(tmp)


    print("YES" if check(a,n) else "NO6 ")