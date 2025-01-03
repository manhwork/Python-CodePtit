class HoaDon : 
    def __init__(self,id,name,old,new):
        self.id = "KH{:02d}".format(id)
        self.name = name 
        self.old = old 
        self.new = new 
        m3 = new - old 
        if m3 <= 50 :
            self.tong = m3 * 100 * 1.02
        elif m3 <= 100 : 
            self.tong = ( 50 * 100 + (m3 - 50) * 150) * 1.03
        else : 
            self.tong = ( 50 * 100 + 50 * 150 + (m3 - 100) * 200) * 1.05


    def __str__(self):
        return "{} {} {:.0f}".format(self.id, self.name, self.tong)
    

result = []

for i in range(1, int(input()) + 1):
    name = input()
    old = int(input())
    new = int(input())
    hd =  HoaDon(i, name, old, new)
    result.append(hd)

result.sort(key=lambda x : -x.tong)

print(*result,sep="\n")


"""
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
"""


