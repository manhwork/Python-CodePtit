from math import * 

class PhanSo : 
    def __init__(self,a,b):
        self.a = a
        self.b = b 

    def __str__(self):
        k = gcd(self.a, self.b) 
        return "{}/{}".format(int(self.a / k) , int(self.b / k))
    

if __name__ == "__main__" :
    a,b = map(int,input().split())
    p = PhanSo(a,b)
    print(p)