from math import * 

def toDecimal(n):
    return int((n),base=2)

if __name__ == "__main__":
    for _ in range(int(input())):
        a = int(input())
        binary_number = input()
        decimal_number = toDecimal(binary_number)
        if(a == 2): print(binary_number)
        elif a == 8 : print("{:o}".format(decimal_number))
        elif a == 10 : print(decimal_number)
        elif a == 16: print("{:X}".format(decimal_number))

# 2
# 8
# 10010100010010101
# 2
# 10010100010010101