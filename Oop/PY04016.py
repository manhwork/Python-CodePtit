from datetime import datetime

class HoaDon : 
    def __init__(self, id, name, sp, nhan, tra, ps):
        self.id = "KH{:02d}".format(id)
        self.name = name 
        self.sp = sp
        self.nhan = datetime.strptime(nhan, "%d/%m/%Y")
        self.tra = datetime.strptime(tra, "%d/%m/%Y") 
        self.ps = ps 
        sn = (self.tra - self.nhan).days + 1
        self.sn = sn 
        if sp[0] == "1":
            self.tong = sn * 25 + ps
        elif sp[0] == "2":
            self.tong = sn * 34 + ps
        elif sp[0] == "3":
            self.tong = sn * 50 + ps
        elif sp[0] == "4":
            self.tong = sn * 80 + ps


    def __str__(self):
        return f"{self.id} {self.name} {self.sp} {self.sn} {self.tong}"
    
result = []

for i in range(int(input())):
    name = input().strip()
    sp = input().strip()
    nhan = input().strip()
    tra = input().strip()
    ps = int(input().strip())
    hd = HoaDon(i + 1, name, sp, nhan, tra, ps)
    result.append(hd)

result.sort(key=lambda x : -x.tong)

print(*result,sep="\n")



"""
3
Huynh Van Thanh   
103 
05/06/2010   
05/06/2010   
15
Le Duc Cong  
106 
08/03/2010   
01/05/2010   
220
Tran Thi Bich Tuyen   
207 
10/04/2010   
21/04/2010   
96
"""

    