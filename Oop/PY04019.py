class SinhVien : 
    def __init__(self,id,name,d1,d2):
        self.id = "TS0" + str(id)
        self.name = name 
        self.d1 = d1 
        self.d2 = d2
        tb = (d1 + d2) /2 
        if tb > 10.0 : self.tb = tb / 10 
        else : self.tb = tb 


    def kq(self, tb):
        if tb < 5 : return "TRUOT"
        if tb < 8 : return "CAN NHAC"
        if tb <= 9.5 : return "DAT"
        
        return "XUAT SAC"

    def __str__(self):
        return "{} {} {:.2f} {}".format(self.id, self.name, self.tb, self.kq(self.tb))
    

result = []

for i in range(int(input())):
    result.append(SinhVien(i+1,input(),float(input()),float(input())))

result.sort(key=lambda x: -x.tb)

print(*result,sep="\n")

"""
3
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
"""