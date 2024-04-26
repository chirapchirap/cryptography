from random import randint
from math import gcd
from crc import crc


def get_k(p):
    for k in range(2, p-1):
        if gcd(k, p-1) == 1:
            return k


p = 127
g = 29
poly = 6

M = 230
r = 14
s = 118

h = int(crc(bin(M)[2:], bin(poly)[2:]), 2)
k = get_k(p)

x = randint(0, p-1)
y = pow(g, x, p)
r = pow(g, k, p)

print("y^r * r^s = g^h mod p :", (y**r * r**s) % p == (g**h) % p)
