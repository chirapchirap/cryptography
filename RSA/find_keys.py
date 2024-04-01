from math import gcd
from gmpy2 import invert
from random import randint


def find_rsa_keys(x):
    while True:
       d = randint(2, x-1)
       if gcd(d, x) == 1:
        e = invert(d, x)
        if gcd(e, x) == 1:
          return(int(e), d)

p = 127
q = 263
n = p*q
euler_func = (p-1)*(q-1)

keys_list = [find_rsa_keys(euler_func) for i in range(3)]

print('(e, n):', list([key[0], n] for key in keys_list))
print('(d, n):', list([key[1], n] for key in keys_list))
