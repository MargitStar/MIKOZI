import sys


def phi_n(p, q):
    return (p - 1) * (q - 1), p * q


def gcd(a, b):
    if b == 0:
        return 1, 0, a
    y, x, g = gcd(b, a % b)
    return x, y - (a // b) * x, g


def module(a, m):
    x, y, g = gcd(a, m)
    if g != 1:
        sys.exit("Error")
    x = (x % m + m) % m
    return x


def bin_pow(a, n, m):
    result = 1
    while n:
        if n & 1:
            result *= a
            result %= m
            n -= 1
        else:
            a *= a
            a %= m
            n >>= 1
    return result


p = 684391453787369
q = 938396705691661
e = 245372344253915653531369256899
x1 = 184712154522842417799563173273
y2 = 447204864183801463638208868116

phi, n = phi_n(p, q)
d = module(e, phi)

y1 = bin_pow(x1, e, n)
x2 = bin_pow(y2, d, n)

print(f"p, {p}")
print(f"q, {q}")
print(f"n, {n}")
print(f"phi, {phi}")
print(f"e ,{e}")
print(f"d, {d}")

print(f"x1, {x1}")
print(f"y1, {y1}")
print(f"x2, {x2}")
print(f"y2, {y2}")
