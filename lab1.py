alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')


# Task 2 (Vigenère cipher)

key = list('ДУЦ')
text = list('ЬЬКФЁЫОЕИ')


def vigenere_cipher_encrypt(alphabet, key, text):
    new_text_indexes = [(alphabet.index(value) + alphabet.index(key[index % len(key)])) % len(alphabet) for index, value in enumerate(text)]

    encoded = ''

    for ind in new_text_indexes:
        encoded += alphabet[ind]

    return encoded

def vigenere_cipher_decrypt(alphabet, key, text):
    new_text_indexes = [alphabet.index(value) - alphabet.index(key[index % len(key)]) % len(alphabet) for index, value in enumerate(text)]

    decoded = ''

    for ind in new_text_indexes:
        decoded += alphabet[ind]

    return decoded

initial_text = ''.join(text)
print(f'Initial text: {str(initial_text)}')

decoded = vigenere_cipher_decrypt(alphabet, key, text)
print(f'Decrypted: {decoded}')

encoded = vigenere_cipher_encrypt(alphabet, key, decoded)
print(f'Encrypted: {encoded}')


