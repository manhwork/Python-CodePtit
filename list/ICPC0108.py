from math import * 



def findTriplets(arr, n):
    found = False
    arr.sort()
    for i in range(0, n-1):
        l = i + 1
        r = n - 1
        x = arr[i]
        while (l < r):
            if (x + arr[l] + arr[r] == 0):
                found = True
                l += 1
                r -= 1
            elif (x + arr[l] + arr[r] < 0):
                l += 1
            else:
                r -= 1
    return found

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if findTriplets(a, n):
        print(1)
    else:
        print(0)

