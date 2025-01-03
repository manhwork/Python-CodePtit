from datetime import datetime

class SinhVien: 
    def __init__(self,name,ns,d1,d2,d3):
        self.name = name 
        self.ns= datetime.strftime(datetime.strptime(ns,"%d/%m/%Y"),"%d/%m/%Y")
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3

    def __str__(self):
        tong = self.d1 + self.d2 + self.d3
        return "{} {} {:.1f}".format(self.name, self.ns, tong)
    
name = input()
ns = input()
d1 = float(input())
d2 = float(input())
d3 = float(input())

sv = SinhVien(name,ns,d1,d2,d3)

print(sv)

"""""
Nguyen Hoang Ha
11/9/2001
4.5
10.0
5.5
"""