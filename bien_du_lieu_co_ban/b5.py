MOD = 10**9 + 7

def mod_comb(n, k, mod=MOD):
    # Hàm tính tổ hợp C(n, k) theo modulo
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    num = den = 1
    for i in range(k):
        num = num * (n - i) % mod
        den = den * (i + 1) % mod
    return num * pow(den, mod - 2, mod) % mod

def solve(N, K, A):
    A.sort()
    result = 0
    
    # Tính tổng đóng góp khi A[i] là lớn nhất và nhỏ nhất
    for i in range(N):
        max_contrib = mod_comb(i, K - 1)  # Số lần A[i] là lớn nhất
        min_contrib = mod_comb(N - i - 1, K - 1)  # Số lần A[i] là nhỏ nhất
        result = (result + A[i] * (max_contrib - min_contrib)) % MOD
    
    return result

# Đọc input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Tính toán và in kết quả
print(solve(N, K, A))
