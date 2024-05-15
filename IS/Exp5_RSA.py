def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def is_prime(n):
    if n < 1:
        return False
    for i in range(2, int(n * 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_keypair(p, q, e):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime")
    elif p == q:
        raise ValueError("p and q cannot be equal")
    
    n = p * q
    phi = (p - 1) * (q - 1)
    while gcd(e, phi) != 1:
        e += 1
    # Compute d, the modular inverse of e
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    key, n = public_key
    # Encrypt the plaintext using the public key
    encrypted_msg = pow(plaintext, key, n)
    return encrypted_msg

def decrypt(private_key, encrypted_msg):
    key, n = private_key
    # Decrypt the ciphertext using the private key
    decrypted_msg = pow(encrypted_msg, key, n)
    return decrypted_msg

p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))
e = int(input("Enter a value for e: "))
plaintext = int(input("Enter the plaintext to encrypt (as a number): "))

public_key, private_key = generate_keypair(p, q, e)
print("Public key:", public_key)
print("Private key:", private_key)

encrypted_msg = encrypt(public_key, plaintext)
decrypted_msg = decrypt(private_key, encrypted_msg)
print("Encrypted message:", encrypted_msg)
print("Decrypted message:", decrypted_msg)