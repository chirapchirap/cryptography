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
