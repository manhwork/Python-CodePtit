class SinhVien : 
    def __init__(self,name,a,b):
        self.name = name 
        self.a = a 
        self.b = b

    def __str__(self):
        return "{} {} {}\n".format(self.name, self.a, self.b)


result = []

for _ in range(int(input())):
    name = input()
    a,b = map(int,input().split())
    sv = SinhVien(name,a,b)
    result.append(sv)

result.sort(key= lambda x : (-x.a, x.b, -x.name))
for x in result :  
    print(x)


# 2
# Nguyen Van Nam
# 168 600
# Tran Thi Ngoc
# 168 600