import re

s = ""


for _ in range(int(input())):
    s += input().strip().lower() +  ' '

wordList = re.findall(r"[a-zA-Z]+",s)

map = dict()

for x in wordList : 
    if x in map : 
        map[x] += 1
    else : 
        map[x] = 1


result = sorted(map.items(),key= lambda x : (-x[1],x[0]))

for x in result : 
    print(x[0], x[1])


"""""
3
PTIT duy tri hoc phi on dinh nam as2019ass va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
"""""