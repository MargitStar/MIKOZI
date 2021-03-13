X = '00010000'
INIT_KEY = '110110001010'
S_1 = {'0': 9, '1': 6, '2': 3, '3': 2, '4': 8,
       '5': 'b', '6': 1, '7': 7, '8': 'a', '9': 4,
       'a': 'e', 'b': 'f', 'c': 'c', 'd': 0, 'e': 'd',
       'f': 5}
S_2 = {'0': 1, '1': 'd', '2': 2, '3': 9, '4': 7,
       '5': 'a', '6': 6, '7': 0, '8': 8, '9': 'c',
       'a': 4, 'b': 5, 'c': 'f', 'd': 3, 'e': 'b',
       'f': 'e'}
indexes = [[1, 2, 3, 4, 5, 6, 7, 8],
           [6, 7, 8, 9, 10, 11, 12, 1],
           [11, 12, 1, 2, 3, 4, 5, 6]]
block_p = [7, 8, 1, 2, 3, 4, 5, 6]


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

def add_zeros(val, n):
    if len(val) % n:
        val = '0' * (n - len(val) % n) + val
    return val


def sp_substitution(x_):
    for i in range(0, 3):
        round_key = ''
        for j in indexes[i]:
            round_key = round_key + INIT_KEY[j - 1]

        t = bin(int(x_, 2) ^ int(round_key, 2))[2:]

        t = add_zeros(t, 8)

        t_blocks_array = list(chunks(t, 4))

        t_1 = t_blocks_array[0]
        t_2 = t_blocks_array[1]

        n_1 = bin(int(str(S_1.get(hex(int(t_1, 2))[2:])), 16))[2:]
        n_2 = bin(int(str(S_2.get(hex(int(t_2, 2))[2:])), 16))[2:]

        n_1 = add_zeros(n_1, 4)
        n_2 = add_zeros(n_2, 4)

        n = n_1 + n_2

        y = ''
        for j in block_p:
            y = y + n[j - 1]
        x_ = y

        print('\tResult at ' + str(i + 1) + ' iterations:', y)

print('Results for the initial message:')
x_1 = X
sp_substitution(x_1)

print('\nResults after replacing one bit of the initial message:')
x_2 = list(X)
# Change the 8-th bit
x_2[7] = str(1 - int(x_2[7]))
x_2 = ''.join(x_2)
sp_substitution(x_2)

