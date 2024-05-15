def vigenere(plaintext, key, encrypt = True):
    result = ""
    key_index = 0
    factor = 1 if encrypt else -1

    for char in plaintext:
        if char.isalpha():
            char = char.upper()
            key_char = key[key_index % len(key)].upper()
            encrypted_char = chr(((ord(char) + factor * ord(key_char) - 2 * ord('A')) % 26) + ord('A'))
            key_index += 1
            result += encrypted_char
        else:
            result += char
    return result

plaintext = str(input("Enter plaintext: "))
key = str(input("Enter key: "))

encrypted_text = vigenere(plaintext, key)
decrypted_text = vigenere(encrypted_text, key, encrypt = False)

print("Original Text: ", plaintext)
print("Encrypted Text: ", encrypted_text)
print("Decrypted Text: ", decrypted_text)