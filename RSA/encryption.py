encoding = [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 99],
            ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ']]

def get_blocks(data, n):
    mod_length = len(str(n))
    blocks = list()
    while True: 
        if len(data) == 0: 
            return blocks
        if len(data) < mod_length:
            block_slice = data[:len(data)]
        else:
            block_slice = data[:mod_length]
        if int(block_slice) > n:
            block_slice = data[:mod_length-1]
            blocks.append(block_slice)
            data = data.replace(data[:len(block_slice)], "", 1)
        else:
            blocks.append(block_slice)
            data = data.replace(data[:len(block_slice)], "", 1)    

def fast_pow(x, y):
    s, v, c = 1, y, x
    while (v > 0):
        if (v % 2 == 1):
            s = s * c
        v = v >> 1
        c = c * c
    return s

enc_key = [10925, 33401]

msg = 'Я хочу чтобы моя программа правильно отработала'
msg_upper = msg.upper()

data = ''.join(map(str, (encoding[0][encoding[1].index(let)] for let in msg_upper)))
print("Исходный текст:", msg_upper)
print("Исходный текст в кодировке:", data)
blocks = get_blocks(data, enc_key[1])
print("Блоки:", blocks)
enc_data = ''.join(map(str, map(lambda x: (fast_pow(int(x),enc_key[0])) % enc_key[1], blocks)))
print("Зашифрованный текст:", enc_data)
