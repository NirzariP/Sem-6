def remove_spaces(text):
    return ''.join(text.split())

def pad_text(text, key_length):
    padding_length = key_length - (len(text) % key_length)
    if padding_length != key_length:
        text += 'X' * padding_length
    return text

def encrypt(plaintext, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    encrypted_text = ''
    plaintext = remove_spaces(plaintext)
    plaintext = pad_text(plaintext, len(key))
    for i in key_order:
        encrypted_text += ''.join(plaintext[i::len(key)])
    return encrypted_text

def decrypt(encrypted_text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    cols = len(encrypted_text) // len(key)
    plaintext = [''] * len(encrypted_text)
    pos = 0
    for i in key_order:
        for j in range(cols):
            plaintext[i + j * len(key)] = encrypted_text[pos]
            pos += 1
    plaintext = ''.join(plaintext)
    # Trim bogus 'X' characters
    plaintext = plaintext.rstrip('X')
    return plaintext


plaintext = "wearediscoveredfleeatonce"
key = "zebras"

encrypted_text = encrypt(plaintext, key)
print("Cipher text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)