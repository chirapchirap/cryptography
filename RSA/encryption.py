encoding = [['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '99'],
            ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ']]

def check_block(b):
    tmp = b[len(b)-1:len(b)]
    while int(tmp) == 0:
        b = b[:len(b)-1]
        tmp = b[len(b)-1:len(b)]
    else:
        return b
    # tmp = b[len(b)-1:len(b)]
    # b = b[:len(b)-1]
    # if int(tmp) == 0:
    #     if int(b[len(b)-1:len(b)]) == 0:
    #         b = b[:len(b)-2]
    #     else:
    #         b = b[:len(b)-1]
        
    # else:
        

    # while True:
    #     if int(b[-1]) == 0 and int(b[-2]) == 0:
    #         b = b[:len(b)-3]
    #     elif int(b[-1]) == 0 and int(b[-2]) != 0:
    #         b = b[:len(b)-2]
    #     elif len(b) > m_l:
    #         b = b[:m_l]
    #         return b
    #     else:
    #         return b

def get_blocks(data, n):
    mod_length = len(str(n))
    blocks = list()
    while True: 
        if len(data) == 0: 
            return blocks
        elif len(data) <= mod_length:
            block_slice = data[:len(data)]
        else:
            block_slice = data[:mod_length+1]
            block_slice = check_block(block_slice)
        if int(block_slice) > n:
            length = len(block_slice)-mod_length
            block_slice = block_slice[:len(block_slice)-length]
            checked_block = check_block(block_slice)
            blocks.append(checked_block)
            data = data.replace(data[:len(block_slice)], "", 1)
        else:
            blocks.append(block_slice)
            data = data.replace(data[:len(block_slice)], "", 1)    


if __name__ == "__main__":
    enc_key = []

    msg = ''
    msg_upper = msg.upper()

    num_msg = ''.join((encoding[0][encoding[1].index(let)] for let in msg_upper))
    print("Plaintext:", msg_upper)
    print("Plaintext in encoding:", num_msg)
    blocks = get_blocks(num_msg, enc_key[1])
    print("Plaintext' blocks:", blocks)
    enc_msg = ''.join(map(lambda x: str(pow(int(x),enc_key[0], enc_key[1])), blocks))
    print("Ciphertext:", enc_msg)

