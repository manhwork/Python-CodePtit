n, k = map(int, input().split())
a = list(set(map(int, input().split())))
a = sorted(a)
n = len(a)

x = [0] * 100

def sout():
    for i in range(1, k + 1):
        print(a[x[i] - 1], end=' ')
    print()

def ql(i):
    for j in range(x[i - 1] + 1, n - k + i + 1):
        x[i] = j
        if i == k:
            sout()
        else:
            ql(i + 1)

ql(1)


"""
8 3
2 4 4 3 5 1 3 4
"""