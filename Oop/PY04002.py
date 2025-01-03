
class Rectangle : 
    def __init__(self, a, b, c):
        self.a = a 
        self.b = b
        self.c = c

    def perimeter(self):
        return (self.a + self.b) * 2 

    def area(self):
        return self.a * self.b 

    def color(self):
        s = self.c.lower()
        return s[:1].upper() + s[1:]


if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), (arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))