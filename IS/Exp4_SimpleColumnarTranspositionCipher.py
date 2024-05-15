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
    return ''.join(plain_text)

# Example usage
plaintext = "wearediscoveredfleeatonce"
key = "zebras"

cipher_text = encrypt(plaintext, key)
print("Cipher text:", cipher_text)

decrypted_text = decrypt(cipher_text, key)
print("Decrypted text:", decrypted_text)