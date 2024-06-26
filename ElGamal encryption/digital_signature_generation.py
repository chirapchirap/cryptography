from crc import crc
from random import randint
from math import gcd


def get_k(p):
    for k in range(2, p-1):
        if gcd(k, p-1) == 1:
            return k


def get_inverted_k(k, p):
    for k_inverted in range(2, p-1):
        if (k_inverted*k) % (p-1) == 1:
            return k_inverted


poly = 6
M = 230

p = 127
g = 29
x = 3
y = pow(g, x, p)
h = int(crc(bin(M)[2:], bin(poly)[2:]), 2)
k = get_k(p)
r = pow(g, k, p)
u = (h - x*r) % (p-1)
s = (get_inverted_k(k, p) * u) % (p-1)

print(f"(M, r, s): ({M}, {r}, {s})")
