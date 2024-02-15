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

# Подсчет количества битов в одном периоде      
def get_binary_prng_length(bits):
    bits_count= 0
    for bit in bits:
        bits_count += len(str(bit))
    return bits_count
#

#Конвертация десятичных чисел в двоичное представление
def convert_int_to_bin(x):
    return bin(x)[2:].zfill(8)
#

# Подсчет количества четных, нечетных чисел
def count_even_odd_binary_numbers(binary_numbers):
    odd_count = sum(1 for number in binary_numbers if int(number[-1]) == 1)
    even_count = len(binary_numbers) - odd_count
    return odd_count, even_count
#

def count_one_and_zeros_in_bits_sequence(bits):
    zero_count = bits.count("0")
    one_count = len(bits) - zero_count
    return zero_count, one_count

# Вызов функций
prng = loop(a, c, m, x0)       
print("1.Последовательность =", prng)
binary_numbers = list(map(convert_int_to_bin, prng))
print("2.Количество битов =", get_binary_prng_length(binary_numbers))
print("3.Количество нечетных, четных чисел =", count_even_odd_binary_numbers(binary_numbers))
print("4.Количество 0, 1 =", count_one_and_zeros_in_bits_sequence("".join(binary_numbers)))
#