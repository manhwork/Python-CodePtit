# a = input()

# n = len(a)

# check = [False] * (n + 1)
# b = [0] * (n + 1)

# def sout():
#     for i in range(1, n + 1):
#         print(a[b[i] - 1], end="")
#     print()

# def Try(i):
#     for j in range(1, n + 1):
#         if check[j]:
#             continue

#         check[j] = True
#         b[i] = j  

#         if i == n:
#             sout()
#         else:
#             Try(i + 1)
#         check[j] = False

# Try(1)

from itertools import permutations

s = input()

for x in (list(permutations(s))) :
    print("".join(x))