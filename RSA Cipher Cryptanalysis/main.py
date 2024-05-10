from random import randint
from math import gcd


public_key: int = (251, 37901)
cipher_text: int = 239


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  # Modular inverse does not exist
    else:
        return (x % m + m) % m


def factorize_num(num: int):
    x: int = randint(1, num-2)
    y: int = 1
    i: int = 0
    stage: int = 2
    while gcd(num, abs(x-y)) == 1:
        if i == stage:
            y = x
            stage *= 2
        x = (x*x + 1) % num
        i += 1
    p1: int = gcd(num, abs(x-y))
    return (p1, num//p1)


p, q = factorize_num(public_key[1])

euler_func = (p-1)*(q-1)

d = mod_inverse(public_key[0], euler_func)

plain_text = pow(cipher_text, d, public_key[1])

print(f"Простые множители числа N: {p}, {q}")
print(f"Открытый ключ e: ({public_key[0]},{public_key[1]})")
print(f"Закрытый ключ d: ({d},{public_key[1]})")
print(f"Зашифрованный текст: {cipher_text}")
print(f"Расшифрованный текст: {plain_text}")
