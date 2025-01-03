import re 

n, k = map(int,input().split())

s = ""

for _ in range(n):
    s += input().strip().lower() + " "

lineList = re.findall(r"[\w]+",s)

map = dict()

for x in lineList : 
    if x in map : 
        map[x] += 1
    else : 
        map[x] = 1

newMap = {}

for key, val in map.items() : 
    if val >= k : 
        newMap[key] = val

result = sorted(newMap.items(),key= lambda x : (-x[1],x[0]))

for x in result : 
    print(x[0], x[1])

"""""
3 2
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
"""