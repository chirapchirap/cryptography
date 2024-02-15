a, c, m, x0 = 41, 11, 163, 8

# Линейный конгруэнтный ГПСП
def generator(a, c, m, Xn): 
    return ((a*Xn + c) % m)
#

#Конвертация десятичных чисел в двоичное представление
def convert_int_to_bin(x):
    return bin(x)[2:].zfill(8)
#

# Выработка псевдослучайной последовательности
def loop(a, c, m, x0):          
    x1 = x0
    bits_count, odd_count, even_count, zero_count, one_count = 0, 0, 0, 0, 0
    sequence = list()
    while(True):
        sequence.append(x1)
        binary_x1 = convert_int_to_bin(x1)
        bits_count += len(str(binary_x1))
        zero_count += binary_x1.count("0")
        one_count += binary_x1.count("1")
        if (int(binary_x1[-1]) == 1):
            odd_count += 1
        else: 
            even_count += 1
        x2 = generator(a, c, m, x1)
        if x2 == x0:
            return [sequence, bits_count, [odd_count, even_count], [zero_count, one_count]]
        x1 = x2
#
result = loop(a, c, m, x0)
print("1.Последовательность =", result[0])
print("2.Количество битов в одном периоде =", result[1])
print("3.Количество нечетных, четных чисел =", result[2])
print("4.Количество 0, 1 =", result[3])