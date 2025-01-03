<<<<<<< HEAD
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

=======
n, k = map(int, input().split())
a = sorted(map(int, input().split()))
mod = 1000000007
def pow(a, b):
    if b==0: return 1
    if b&1: return pow(a, b-1)*a % mod
    p = pow(a, b>>1)
    return p*p % mod
def inv(i): return pow(i, mod-2)
G = [0]*(n+1)
G[0] = 1
for i in range(1,n+1): G[i] = i*G[i-1] % mod
def C(N, R): return G[N] * inv(G[R]) % mod * inv(G[N-R]) % mod
ans, s = 0, 0
for i in range(n-k+1):
    s = (s + a[n-i-1] - a[i]) % mod
    ans = (ans + C(n-2-i, k-2) * s) % mod
if k==1: print(0)
else: print(ans)
>>>>>>> f5150f204915e23e7eca8fe4c95075a65ca53f59
