s = input()
number = s.split(" ")
print("YES" if int(number[0]) + int(number[2]) == int(number[4]) else "NO")