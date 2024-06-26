import collections


def xor(a, b):
    return ''.join(map(lambda x, y: str(int(x) ^ int(y)), a, b))


def crc(data, gx):
    gx_len = len(gx)

    data += '0' * gx_len
    num = data[:gx_len]
    if len(str(int(data))) < gx_len:
        return str(int(num))
    data = data.replace(data[:gx_len], "", 1)
    while True:
        remainder = str(int(xor(num, gx)))
        if remainder == '0':
            if len(data) <= gx_len and int(data) == 0:
                return remainder
            num = data[:gx_len]
            data = data.replace(data[:gx_len], "", 1)
            if len(num) < gx_len:
                return num
        else:
            remainder_len = gx_len - len(remainder)
            num = remainder + data[:remainder_len]
            data = data.replace(data[:remainder_len], "", 1)
            if len(num) < gx_len:
                return num


def detect_crc_collision(iter, gx):
    res = {}
    for num in range(0, iter):
        temp = crc(bin(num)[2:], gx)
        if res.keys().__contains__(temp):
            res[temp].append(num)
        else:
            res[temp] = []
            res[temp].append(num)
    return res


def dict_output(dictionary):
    dictionary = collections.OrderedDict(sorted(dictionary.items()))
    for key in dictionary.keys():
        items = dictionary[key]
        print(f"{key}: {items}")
    return


if __name__ == '__main__':
    # Fuse_150, Zlobny_kot, сюда вставляете ваше значение
    generating_polynomial = 0b000000000
    input_data = 0b00000000  # и сюда тоже
    print(f'CRC({bin(input_data)[2:]}) =', crc(
        bin(input_data)[2:], bin(generating_polynomial)[2:]))
    dict_output(detect_crc_collision(256, bin(generating_polynomial)[2:]))
