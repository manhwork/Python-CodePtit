
import re
s = ""

for _ in range(int(input())):
    s += input().lower().strip() + ' '

arr = re.findall(r'[\w]+', s)

tmp = dict()

for x in arr : 
    if x in tmp : 
        tmp[x] += 1
    else: 
        tmp[x] = 1


result = sorted(tmp.items(),key=lambda x : (-x[1],x[0],))

for item in result: 
    print(item[0],item[1])

"""""
3
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
"""