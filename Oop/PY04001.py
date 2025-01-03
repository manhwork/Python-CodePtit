from decimal import Decimal
from math import * 

class Point : 
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def distance(self, p):
        x1 = self.x - p.x 
        y1 = self.y - p.y 
        result = sqrt(x1 * x1 + y1 * y1)
        return "{:.4f}".format(result)
    




if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1

# 2
# 0 0 0 5
# 0 199 5 6