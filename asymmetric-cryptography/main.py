from operator import mod
import random
from xmlrpc.client import boolean


def get_start_value(x: int) -> int:
    while True:
        value = random.randint(1, x - 1)
        if is_prime(value):
            return value


def is_prime(number: int) -> bool:
    if number % 2 == 0:
        return number == 2

    d = 3
    while d * d <= number and number % d != 0:
        d += 2

    return d * d > number


def get_public_key(a: int, g: int, p: int) -> int:
    result = g
    while (a > 0):
        result = result * g % p
        a = a - 1

    return result


def gcd(left: int, right: int) -> int:
    while left != right:
        if left > right:
            left = left - right
        else:
            right = right - left

    return left


def root(modulo: int) -> int:
    r_set = set(num for num in range(1, modulo) if gcd(num, modulo) == 1)
    for g in range(1, modulo):
        a_set = set(pow(g, powers) % modulo for powers in range(1, modulo))
        if r_set == a_set:
            return g


def result(a, b, g, A, B, A_key, B_key, p) -> None:
    print(f'''
          Alice:
          Private key: {str(a)},
          Random param: {str(p)},
          Primitive root: {str(g)}
          Public key: {str(A)},
          Key info: {str(A_key)},
          Bob:
          Private key: {str(b)},
          Random param: {str(p)},
          Primitive root: {str(g)}
          Public key: {str(B)},
          Key info: {str(B_key)},
          ''')


def main():
    p = int(input())
    g, A_private, B_private = root(p), get_start_value(p), get_start_value(p)
    A_public = get_public_key(A_private, g, p)
    B_public = get_public_key(B_private, g, p)
    A_key = get_public_key(A_private, B_public, p)
    B_key = get_public_key(B_private, A_public, p)

    result(A_private, B_private, g, A_public, B_public, A_key, B_key, p)


main()
