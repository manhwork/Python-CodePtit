class HocSinh : 
    def __init__(self, id, name, tb ):
        self.id = "HS{:02d}" .format(id)
        self.name = name 
        self.tb = tb

    def hl(self, tb):
        if tb <5 : return "YEU"
        if tb <7  : return "TB"
        if tb <8  : return "KHA"
        if tb <9  : return "GIOI"
        return "XUAT SAC"
    

    def __str__(self):
        return "{} {} {:.1f} {}".format(self.id,self.name,self.tb,self.hl(self.tb))
    
map = []

for i in range(int(input())):
    name = input()
    diem = input().split()
    diem = [float(x) for x in diem]

    tb = 0
    for x in diem : 
        tb += x
    
    tb += (diem[0] + diem[1])
    tb /= 10
    tb /= 1.2
    map.append(HocSinh(i+1,name,tb))
map.sort(key= lambda x: -x.tb)
for x in map : 
    print(x)

""""
3
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
"""