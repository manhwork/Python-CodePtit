t = int(input())
# 2
# 12ab29cd19
# ab123gh456cd
for _ in range(t):
    s = input() + "#"
    numbers = []
    number = ""
    for i in range(len(s)):
        if s[i].isdigit() : 
            number += s[i]
        else :
            if number != "":
                numbers.append(int(number))
                number = ""
    print(min(numbers))
