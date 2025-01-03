import re 

s = ""

while True : 
    try: 
        s += input().strip().lower()
    except : break

a = re.findall("[\w\s:,]+",s)


for x in a : 
    tmp = x.split()
    tmp[0] = tmp[0].title()
    print(" ".join(tmp))

"""""
ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!
    vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11.
"""