# 1+ x^2 + x^5
# 100100

def xor(a, b):
    return ''.join(map(lambda x, y: str(int(x) ^ int(y)), a, b))


def crc(data, gx):
    gx_len = len(gx)
    data += '0' * gx_len
    num = data[:gx_len]
    data = data.replace(data[:gx_len], "", 1)
    while True:
        remainder = str(int(xor(num, gx)))
        if remainder == '0':
            num = data[:gx_len]
            data = data.replace(data[:gx_len], "", 1)
        else:
            remainder_len = gx_len - len(remainder)
            num = remainder + data[:remainder_len]
            data = data.replace(data[:remainder_len], "", 1)
            if len(num) < gx_len:
                return num


if __name__ == '__main__':
    input_data = 0b11100101
    generating_polynomial = 0b100100
    res = crc(bin(input_data)[2:], bin(generating_polynomial)[2:])
    print(res)
