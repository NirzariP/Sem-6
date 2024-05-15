def remove_spaces(text):
    return ''.join(text.split())

def pad_text(text, key_length):
    padding_length = key_length - (len(text) % key_length)
    if padding_length != key_length:
        text += 'X' * padding_length
    return text

def encrypt(plain_text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    cipher_text = ''
    plain_text = remove_spaces(plain_text)
    plain_text = pad_text(plain_text, len(key))
    for i in key_order:
        cipher_text += ''.join(plain_text[i::len(key)])
    return cipher_text

def decrypt(cipher_text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    cols = len(cipher_text) // len(key)
    plain_text = [''] * len(cipher_text)
    pos = 0
    for i in key_order:
        for j in range(cols):
            plain_text[i + j * len(key)] = cipher_text[pos]
            pos += 1
    plain_text = ''.join(plain_text)
    # Trim bogus 'X' characters
    plain_text = plain_text.rstrip('X')
    return plain_text

plaintext = "wearediscoveredfleeatonce"
key1 = "zebras"
key2 = "hi"

cipher_text1 = encrypt(plaintext, key1)
cipher_text2 = encrypt(cipher_text1, key2)
print("Cipher text:", cipher_text2)

decrypted_text1 = decrypt(cipher_text2, key2)
decrypted_text2 = decrypt(decrypted_text1, key1)
print("Decrypted text:", decrypted_text2)