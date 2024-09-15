n = int(input())
a = list(map(int,input().split()))
# 5
# 2 3 4 5 6
# 10
# 1 5 5 8 6 4 3 5 9 3
stack = []
for x in a : 
    if len(stack) != 0 and (stack[-1] + x) % 2 == 0 :
        stack.pop()
    else :
        stack.append(x)

print(len(stack))