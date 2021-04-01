import random
import sys

from hashlib import sha256

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

def gen(q):
    while True:
        t = 4 * (q + 1)
        R = random.randint(1, t)
        p = q * R + 1
        if bin_pow(2, q * R, p) != 1 or bin_pow(2, R, p) == 1:
            continue
        else:
            break
    
    while True:
        x = random.randint(1, p)
        g = bin_pow(x, R, p)
        if g == 1:
            continue
        else:
            break

    d = random.randint(1, q)
    e = bin_pow(g, d, p)

    return p, q, g, e, d

def sign(p, q, g, d):
    m = int(sha256(message.encode('utf-8')).hexdigest(),16)
    k = random.randint(1, q)
    r = bin_pow(g, k, p)
    s = (module(k, q) * ((m - d * r) % q + q)) % q
    return r, s

def verify(p, q, g):
    if r == 0 and r >= p or s >= q:
        return False
    m = int(sha256(message.encode('utf-8')).hexdigest(),16)
    
    if (bin_pow(e, r, p) * bin_pow(r, s, p)) % p != bin_pow(g, m, p):
        return False

    return True

q = 71377667593522809398065817488727894625089268662066515584888587607032916396479
message = "Я, Маргарита Бобкова, люблю МиКОЗИ"

p, q, g, e, d = gen(q)
r, s = sign(p, q, g, d)
print(verify(p, q, g))
