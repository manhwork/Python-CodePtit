from math import gcd

class PhanSo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def rutgon(self):
        k = gcd(self.a, self.b)
        self.a = self.a // k
        self.b = self.b // k

    def cong(self, p):
        tu = self.a * p.b + p.a * self.b
        mau = self.b * p.b
        ket_qua = PhanSo(tu, mau)
        ket_qua.rutgon()
        return ket_qua

    def __str__(self):
        return f"{self.a}/{self.b}"

if __name__ == "__main__":
    a1, b1, a2, b2 = map(int, input().split())
    ps1 = PhanSo(a1, b1)
    ps2 = PhanSo(a2, b2)
    ket_qua = ps1.cong(ps2)
    print(ket_qua)
