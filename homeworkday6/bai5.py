from math import *
def tich(s, n):
    tu = 1
    mau = 1
    for i in range(0, n):
        tu *= s[i][0]
        mau *= s[i][1]
    return tu, mau
def toiGian(a, b):
    x = gcd(a, b)
    a //= x
    b //= x
    return a, b
n = int(input())
s = []
for i in range(0, n):
    ab = list(map(int, input().split()))
    s.append(ab)
tu, mau = tich(s, n)
tu, mau = toiGian(a=tu, b=mau)
print(tu, mau)