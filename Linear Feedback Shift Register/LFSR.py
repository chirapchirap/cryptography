def realize_xor(bits):
    if len(bits) == 0:
        return None
    elif len(bits) == 1:
        return None
    elif len(bits) == 2:
        return bits[0] ^ bits[1]
    elif len(bits) % 2 == 0:
        for i in range(0, len(bits), 2):
            if i == 0:
                res = bits[i] ^ bits[i+1]
            else:
                res ^= bits[i] ^ bits[i+1]
        return res
    else:
        for i in range(0, len(bits)-1, 2):
            if i == 0:
                res = bits[i] ^ bits[i+1]
            else:
                res ^= bits[i] ^ bits[i+1]
        return res ^ bits[-1]


def wrap_bits_seq_by_8(bits):
    x = 8
    wrapped_code = [bits[y-x:y] for y in range(x, len(bits)+x, x)]
    return wrapped_code


def count_odd_and_even(list_of_bits):
    odd_count, even_count = 0, 0
    wrapped_bits = wrap_bits_seq_by_8(''.join(map(str, list_of_bits)))
    for bit in wrapped_bits:
        if (int(bit[-1]) == 1):
            odd_count += 1
        else:
            even_count += 1
    return [odd_count, even_count]


def get_lfsr(st, char_poly_bits):
    x1 = st.copy()
    bits_for_xor = list(bit for index, bit in enumerate(x1)
                        if index in char_poly_bits)
    zero_count = 0
    one_count = 0
    sequence = list()
    while (True):
        print(x1, end='')
        x1.insert(0, realize_xor(bits_for_xor))
        popped_bit = x1.pop()
        print(f" -> {popped_bit}")
        sequence.append(popped_bit)
        bits_for_xor = list(bit for index, bit in enumerate(x1)
                            if index in char_poly_bits)
        if popped_bit == 1:
            one_count += 1
        else:
            zero_count += 1
        if x1 == st:
            return [sequence, len(sequence), count_odd_and_even(sequence), [zero_count, one_count]]


def get_polynom_degrees(poly):
    '''
    polynom degrees parser for polynoms represented as 1 + x^... + x^... 
    (... contains degrees numbers)
    '''
    poly = poly.replace(' ', '')
    degrees = []
    i = 0
    while True:
        try:
            i = poly.index('^', i+1, len(poly))
            degrees.append(int(poly[i+1]))
        except:
            return degrees


def get_bits_for_xor_in_lfsr(register_len, degrees):
    '''
    returns degrees for lsfr on the basis of polynom degrees
    '''
    return list(register_len - degree for degree in degrees)


start_value = 0b1101
polynom_string = '1 + x^3 + x^4'
result = get_lfsr(list(map(int, (bin(start_value)[2:]))), get_bits_for_xor_in_lfsr(
    len(bin(start_value)[2:]), get_polynom_degrees(polynom_string)))
print("1.Последовательность =", result[0])
print("2.Количество битов в одном периоде =", result[1])
print("3.Количество нечетных, четных чисел =", result[2])
print("4.Количество 0, 1 =", result[3])
