# F(x) = 1 + x^2 + x^4 + x^8
i1, i2, i3 = -2, -4, -8

def wrap_bits_seq_by_8(bits):  
    x=8
    wrapped_code=[bits[y-x:y] for y in range(x, len(bits)+x,x)]
    return wrapped_code

def odd_and_even_count(list_of_bits):
    odd_count, even_count = 0, 0
    wrapped_bits = wrap_bits_seq_by_8(''.join(map(str, list_of_bits)))
    for bit in wrapped_bits:
        if (int(bit[-1]) == 1):
            odd_count += 1
        else: 
            even_count += 1
    return [odd_count, even_count]

def lfsr(st):
    x1 = st.copy()
    zero_count = 0
    one_count = 0
    sequence = list()
    a = 0
    while(True):
        x1.insert(0, x1[i1]^x1[i2]^x1[i3])
        popped_bit = x1.pop()
        sequence.append(popped_bit)
        if popped_bit == 1:
            one_count += 1
        else:
            zero_count += 1
        if x1 == st:
            return [sequence, len(sequence), odd_and_even_count(sequence), [zero_count, one_count]]   

start_value = 0b10010011
result = lfsr(list(map(int, (bin(start_value)[2:]))))
print("1.Последовательность =", result[0])
print("2.Количество битов в одном периоде =", result[1])
print("3.Количество нечетных, четных чисел =", result[2])
print("4.Количество 0, 1 =", result[3])
