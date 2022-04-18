import random


def gcd(a: int, b: int) -> int:
    while (b != 0):
        a, b = b, a % b

    return a


def multiplicative_inverse(e: int, r: int) -> int:
    for i in range(r):
        if (e * i) % r == 1:
            return i


def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return n == 2

    d: int = 3
    while d * d <= n and n % d != 0:
        d += 2

    return d * d > n


def generate_keypair(p: int, q: int):
    if not (is_prime(p) and is_prime(q)):
        print("both numbers must be primes")
        return None

    if p == q:
        print("numbers must be different")
        return None

    n: int = p * q

    phi: int = (p - 1) * (q - 1)

    e: int = random.randrange(1, phi)

    g: int = gcd(e, phi)

    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    # public key is (e, n) and private is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext: str):
    key, n = pk
    # a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(pk, ciphertext: str):
    key, n = pk
    # generate plaintext a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)


def main():
    p: int = 53
    q: int = 97

    print('Generating your public/private keypairs...')
    public, private = generate_keypair(p, q)
    print(f'Public key: {public}. Private key: {private}')
    message = str(input('Enter a message to encrypt with private key: '))
    encrypted_msg = encrypt(private, message)
    print('Encrypted message is:')
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print('Decrypted message is:')
    print(decrypt(public, encrypted_msg))


main()
