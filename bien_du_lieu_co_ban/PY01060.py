from math import * 

for _ in range(int(input())):
    n = input()
    tich = 1
    tong = 0
    ok = 0
    for i in range(0,len(n)):
        if( i % 2 == 0):
            if(n[i] != '0'):
                tich *= int(n[i])
                ok = 1
        else :
            tong += int(n[i])

    if not ok : tich = 0
    print(tich,tong)

# 3
# 12345678
# 20000
# 22334455667788