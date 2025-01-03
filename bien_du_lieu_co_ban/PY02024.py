for _ in range(int(input())):
    n = int(input())
    sum = 0
    if n % 2 == 0 :
        check = True
        for i in range(2, n + 1, 2):
            if check : 
                sum += 1/i
                check = False
            else : 
                sum -= 1/i
                check = True
    else : 
        check = True
        for i in range(1, n + 1, 2):
            if check : 
                sum += 1/i
                check = False
            else : 
                sum -= 1/i
                check = True

    print(f'{sum:.5f}')