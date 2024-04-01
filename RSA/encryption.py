encoding = [['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '99'],
            ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ']]

def check_block(b):
    tmp = b[len(b)-1:len(b)]
    if int(tmp) == 0:
        while int(tmp) == 0:
            b = b[:len(b)-1]
            tmp = b[len(b)-1:len(b)]
        return b[:len(b)-1]
    else:
        return b[:len(b)-1]


def get_blocks(data, n):
    mod_len = len(str(n))
    blocks = list()
    while True: 
        if len(data) == 0: 
            return blocks
        elif len(data) <= mod_len:
            checked_b_slice = data[:len(data)]
        else:
            b_slice = data[:mod_len+1]
            checked_b_slice = check_block(b_slice)  
        if int(checked_b_slice) > n:
            b_slice = b_slice[:mod_len]
            checked_b_slice = check_block(b_slice)
            blocks.append(checked_b_slice)
            data = data.replace(data[:len(checked_b_slice)], "", 1)
        else:
            blocks.append(checked_b_slice)
            data = data.replace(data[:len(checked_b_slice)], "", 1)    


if __name__ == "__main__":
    enc_key = [25223, 33401]

    msg = 'я хочу чтобы моя программа нормально отработала'
    msg_upper = msg.upper()

    num_msg = ''.join((encoding[0][encoding[1].index(let)] for let in msg_upper))
    print("Plaintext:", msg_upper, end='\n\n')
    print("Plaintext in encoding:", num_msg, end='\n\n')
    blocks = get_blocks(num_msg, enc_key[1])
    print("Plaintext' blocks:", blocks, end='\n\n')
    enc_msg = list(map(lambda x: str(pow(int(x),enc_key[0], enc_key[1])), blocks))
    print("Ciphertext:", ''.join(enc_msg), end='\n\n')
    print("Ciphertext in blocks:", enc_msg)
    

