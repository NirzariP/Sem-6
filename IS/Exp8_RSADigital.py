import hashlib

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

def rsa_signature(plaintext, public_key):
    key, n = public_key
    hash_value = hashlib.sha256(plaintext.encode()).hexdigest()
    hash_int = int(hash_value, 16) % n
    signature = pow(hash_int, key, n)
    return signature

def rsa_verification(plaintext, private_key, signature):
    key, n = private_key
    hash_value = hashlib.sha256(plaintext.encode()).hexdigest()
    hash_int = int(hash_value, 16) % n
    decrypted_msg = pow(signature, key, n)
    if decrypted_msg == hash_int:
        print("success")
    else:
        print("fail")
    # return decrypted_msg

p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))
e = int(input("Enter a value for e: "))
plaintext = str(input("Enter the plaintext: "))

public_key, private_key = generate_keypair(p, q, e)
print("Public key:", public_key)
print("Private key:", private_key)

signature = rsa_signature(plaintext, public_key)
verification = rsa_verification(plaintext, private_key, signature)
print("Digital Signature:", signature)