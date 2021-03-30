from helpers import *

rslos1 = [
    [0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1]
]
s1 = get_sequence(*rslos1)

rslos2 = [
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 1]
]
s2 = get_sequence(*rslos2)

rslos3 = [
    [1, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1]
]
s3 = get_sequence(*rslos3)

n = 10000
geffe = get_geffe(n, s1, s2, s3)

ones = sum(geffe)
zeros = n - ones
print(f'Ones: {ones}')
print(f'Zeros: {zeros}')

for i in range(1, 6):
    r = 0
    for j in range(n - i):
        r += (-1) ** (geffe[j] ^ geffe[j + i])
    print(f'r{i} = {r}')