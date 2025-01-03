class SinhVien:
    def __init__(self, id, name, lop, stt):
        self.id = id 
        self.name = name 
        self.lop = lop 
        self.stt = stt



    def __str__(self):
        return f"{self.id} {self.name} {self.lop}"
    

class DanhSach:
    def __init__(self, sv, ma):
        self.sv = sv 
        self.ma = ma 
        tong = 10 
        for x in ma :
            if x == "m": tong -= 1
            elif x == "v": tong -= 2
        
        self.gc = ""

        if tong <= 0 : 
            tong = 0
            self.gc = "KDDK"

        self.tong = tong


    def __str__(self):
        return  f"{self.sv} {self.tong} {self.gc}"
    
svMap = {}

n = int(input())

for i in range(n):
    id = input()
    sv = SinhVien(id,input(),input(),i)
    svMap[id] = sv

dsList = []

for _ in range(n):
    id, ma = input().split()
    ds = DanhSach(svMap[id], ma)
    dsList.append(ds)
dsList.sort(key=lambda x: x.sv.stt)


print(*dsList,sep="\n")

"""
3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
"""