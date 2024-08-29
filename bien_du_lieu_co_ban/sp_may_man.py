from math import *
s = input()
num4 = [x for x in s if x == '4']
num7 = [x for x in s if x == '7']
print("YES" if (len(num4) + len(num7) == 4 ) or (len(num4) + len(num7) == 7 ) else "NO")
