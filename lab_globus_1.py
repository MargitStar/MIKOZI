alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

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
