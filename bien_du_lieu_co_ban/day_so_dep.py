def count_insert(a):
    cnt = 0
    for i in range(len(a)-1):
        x, y = min(a[i],a[i+1]), max(a[i],a[i+1])
        while y > 2*x : 
            x*= 2 
            cnt += 1

    return cnt 

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    print(count_insert(a))