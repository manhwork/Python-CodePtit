class ThoiGian : 
    def __init__(self,id ,name, start, end):
        self.id = id 
        self.name = name 
        self.start = start 
        self.end = end 
        self.time = self.Time(start, end)
        self.svtime = "{} gio {} phut".format(self.time // 60, self.time - (self.time // 60) * 60)



    def Time(self, start, end):
        start = list(map(int, start.split(":")))
        end = list(map(int, end.split(":")))

        return - (start[0] * 60 + start[1]) + (end[0]*60 + end[1])
    
    def __str__(self):
        return "{} {} {}".format(self.id, self.name,self.svtime)

result = []

for _ in range(int(input())):
    result.append(ThoiGian(input(),input(),input(),input()))


result.sort(key=lambda x : -x.time)

print(*result,sep="\n")

"""
3
01T
Nguyen Van An
09:00
10:30
06T
Hoang Van Nam
15:30
18:00
02I
Tran Hoa Binh
09:05
10:00
"""