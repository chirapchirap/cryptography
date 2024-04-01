
encoding = [['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '99'],
            ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ']]



if __name__ == "__main__":
    dec_key = []
    enc_msg_blocks = []
    print("Ciphertext:", ''.join(enc_msg_blocks))
    print("Ciphertext' blocks:", enc_msg_blocks)
    dec_num_blocks = list(map(lambda x: str(pow(int(x), dec_key[0], dec_key[1])), enc_msg_blocks))
    print("Decrypted blocks:", dec_num_blocks)
    dec_num_msg = ''.join(dec_num_blocks)
    print("Decrypted text in encoding:", dec_num_msg)
    dec_data = ''.join(encoding[1][encoding[0].index(num)] for num in [dec_num_msg[i:i+2] for i in range(0, len(dec_num_msg), 2)])
    print("Decrypted text:", dec_data)