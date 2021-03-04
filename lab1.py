import math

alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

# Task 1

# int gcd (int a, int b, int & x, int & y) {
#   if (a == 0) {
#     x = 0; y = 1;
#     return b;
#   }
#   int x1, y1;
#   int d = gcd (b%a, a, x1, y1);
#   x = y1 - (b / a) * x1;
#   y = x1;
#   return d;
# }

def gcd(a, b):
    if not b:
        return (1, 0, a)
    y, x, g = gcd(b, a % b)
    return (x, y - (a // b) * x, g)


def affine_encrypt(text, alphabet, a, b):
    m = len(alphabet)

    encrypted = []

    for char in text:
        encrypted.append(alphabet[((a * alphabet.index(char)) + b) % m])
    return ''.join(encrypted)


def affine_decrypt(text, alphabet, a, b):
    m = len(alphabet)

    decrypted = []

    x, y = 0, 0
    x, y, g = gcd(a, m)
    if g != 1:
        print("Error")
    else:
        x = (x % m + m) % m

    for char in text:
        pos = (x * (alphabet.index(char) - b)) % m
        pos += m if pos < 0 else 0
        decrypted.append(alphabet[pos])

    return "".join(decrypted)

print(f'Initial text: БОБКОВА')


affine_en = affine_encrypt('БОБКОВА', alphabet, 8, 18)
print("Encrypted:", affine_en)

print("Decrypted: ",affine_decrypt(affine_en, alphabet, 8, 18))


# Task 2 (Vigenère cipher)
key = list('ДУЦ')
text = list('ЬЬКФЁЫОЕИ')


def vigenere_cipher_decrypt(alphabet, key, text):
    new_text_indexes = [(alphabet.index(value) + alphabet.index(key[index % len(key)])) %
                        len(alphabet) for index, value in enumerate(text)]

    encoded = ''

    for ind in new_text_indexes:
        encoded += alphabet[ind]

    return encoded


def vigenere_cipher_encrypt(alphabet, key, text):
    new_text_indexes = [alphabet.index(value) - alphabet.index(
        key[index % len(key)]) % len(alphabet) for index, value in enumerate(text)]

    decoded = ''

    for ind in new_text_indexes:
        decoded += alphabet[ind]

    return decoded


initial_text = ''.join(text)
print(f'\nInitial text: {str(initial_text)}')

decoded = vigenere_cipher_encrypt(alphabet, key, text)
print(f'Encrypted: {decoded}')

encoded = vigenere_cipher_decrypt(alphabet, key, decoded)
print(f'Decrypted: {encoded}')
