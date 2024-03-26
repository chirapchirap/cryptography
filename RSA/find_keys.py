from math import gcd
from gmpy2 import invert
from random import randint

def find_coprime_number(x):
    while True:
       coprime_num = randint(2, x-1)
       if gcd(coprime_num, x) == 1:
          return coprime_num

def find_inverse_number_by_mod(x, mod):
    return invert(x, mod)

p = 127
q = 263
n = p*q
euler_func = (p-1)*(q-1)

d_list = [find_coprime_number(euler_func) for i in range(3)]
e_list = list((int(find_inverse_number_by_mod(num, euler_func)) for num in d_list))

print('e:', list([e, n] for e in e_list))
print('d:', list([d, n] for d in d_list))
