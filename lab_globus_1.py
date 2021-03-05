import numpy
import math

alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')


# Task 1
# Hill cipher

text = 'ШЕВЧЕНКО'
key_matrix = numpy.array([
    [30, 8],
    [10, 5]
])


def gcd(a, b):
    if not b:
        return (1, 0, a)
    y, x, g = gcd(b, a % b)
    return (x, y - (a // b) * x, g)



def decrypt_hill(key_matrix, text, alphabet):
    m = len(alphabet)

    determinant = key_matrix[0][0]*key_matrix[1][1] - \
        key_matrix[1][0]*key_matrix[0][1]

    evklid = gcd(determinant, m)

    new_matrix = numpy.array(
        [[key_matrix[1][1], - key_matrix[0][1]], [-key_matrix[1][0], key_matrix[0][0]]])

    matrix_for_decrypt = (new_matrix * evklid[0]) % m
    key = [alphabet.index(char) for char in text]
    new_key = numpy.array_split(key, len(key) / 2)

    text_hill = ''

    for i in range(4):
        p = numpy.dot(new_key[i], matrix_for_decrypt)
        num1 = int(math.fmod(p[0], 33))
        num2 = int(math.fmod(p[1], 33))
        text_hill += alphabet[num1] + alphabet[num2]
    return text_hill


def encrypt_hill(key, text, alphabet):
    decrypted_key = [alphabet.index(char) for char in text]
    decrypted_key_new = numpy.array_split(decrypted_key, len(text)/2)
    
    text_hill = ''
    for i in range(4):
        p = numpy.dot(decrypted_key_new[i], key_matrix)
        num1 = int(math.fmod(p[0], 33))
        num2 = int(math.fmod(p[1], 33))
        text_hill += alphabet[num1] + alphabet[num2]
    return text_hill


print(f'\nInitial text: {text}')
print('Encrypted:', encrypt_hill(key_matrix, text, alphabet))
decrypted_msg = decrypt_hill(key_matrix, 'ЗЪГДЩКСЮ', alphabet)
print('Decrypted:', decrypted_msg)


# Task 2
# Simple replacement

key = list('ОШЧВЦЯПЩГЭДЫМРТЙХЮБЛИЬЁУЕКФЖСАНЗЪ')
text = list('ЧЯЮЙЪЛТЙБЛА')


def simple_replacement_encrypt(alphabet, key, text):
    encoded_list = [key[alphabet.index(value)] for value in text]

    return ''.join(encoded_list)


def simple_replacement_decrypt(alphabet, key, text):
    new_key = [alphabet[key.index(value)] for value in alphabet]  #

    return simple_replacement_encrypt(alphabet, new_key, text)


initial_text = ''.join(text)
print(f'\nInitial text: {initial_text}')

decoded = simple_replacement_decrypt(alphabet, key, initial_text)
print(f'Decrypted: {decoded}')

encoded = simple_replacement_encrypt(alphabet, key, decoded)
print(f'Encrypted: {encoded}')
