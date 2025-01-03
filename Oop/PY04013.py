
luongmuaMap = {}

def time( start, end) : 
    return (end[0] * 60 + end[1]) - (start[0] * 60 + start[1]) 

for _ in range(int(input())):
    name = input()
    start = [int(x) for x in input().split(":")]
    end = [int(x) for x in input().split(":")]

    info = int(input())
    if name in luongmuaMap : 
        luongmuaMap[name] = ( luongmuaMap[name][0] + info ,luongmuaMap[name][1] + time( start, end))
    else : 
        luongmuaMap[name] = ( info ,time( start, end))


cnt = 1 
for x in luongmuaMap.items():
    print("T{:02d}".format(cnt),x[0],"{:.2f}".format(x[1][0] / (x[1][1] / 60)))
    cnt += 1


""""
10
Dong Anh
07:30
08:00
60
Cau Giay
07:45
08:12
50
Soc Son
08:00
09:15
78
Dong Anh
18:50
20:00
88
Cau Giay
19:01
20:00
77
Soc Son
19:06
20:21
66
Dong Anh
21:00
21:40
49
Cau Giay
21:50
22:20
68
Dong Anh
22:15
23:45
30
Cau Giay
22:50
23:45
35
"""