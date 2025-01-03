class MonThi :
    def __init__(self,ma,name,ht):
        self.ma = ma 
        self.name = name 
        self.ht = ht

    def __str__(self) -> str:
        return '{} {} {}'.format(self.ma,self.name,self.ht)
    

l = []
for _ in range(int(input())):
    l.append(MonThi(input(),input(),input()))

l.sort(key=lambda x : x.ma)

print(*l,sep="\n")


# 2
# MUL1320
# Nhap mon da phuong tien
# Bai tap lon + Van dap truc tuyen
# BAS1203
# Giai tich 1
# Thi viet + Van dap truc tuyen