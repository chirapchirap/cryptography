a, c, m, x0 = 41, 11, 163, 8

# Линейный конгруэнтный ГПСП
def generator(a, c, m, Xn): 
    return ((a*Xn + c) % m)
#


# Выработка псевдослучайной последовательности
def loop(a, c, m, x0):          
    x1 = x0
    seq = list()
    seq.append(x0)
    while(True):
        x2 = generator(a, c, m, x1)
        if x2 == x0:
            return seq
        seq.append(x2)
        x1 = x2
#
        
def get_prng_length(bits):
    bits_count= 0
    for bit in bits:
        bits_count += len(str(bit))
    return bits_count

def convert_int_to_bin(x):
    return bin(x)[2:].zfill(8)


prng = loop(a, c, m, x0)       
print(prng, len(prng)*8)
print(get_prng_length(map(convert_int_to_bin, prng)))