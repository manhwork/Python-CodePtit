def base4(s) : 
    base4 = ""
    while s > 0 :
        base4 = str(s%4) + base4
        s//=4
    return base4

for _ in range(int(input())):
    n = int(input())
    s = input()

    tmp = int(s,base=2)


    if n == 2 : 
        print(s)
    elif n == 8 : 
        print("{:o}".format(tmp))
    elif n == 4 :
        print(base4(tmp))
    else : 
        print("{:X}".format(tmp))



"""
3
8
10010100010010101
16
10010100010010101
16
1111
"""