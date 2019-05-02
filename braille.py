alphabet = {'capital': "000001"}


def build_dictionary(plaintext, code):
    split_code = [code[i:i+6] for i in range(0, len(code), 6)]
    i = 0
    for binary in split_code:
        if binary == alphabet['capital']:
            continue
        alphabet[plaintext[i].lower()] = binary
        i += 1


build_dictionary("The quick brown fox jumps over the lazy dog", "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110")


def answer(plaintext):
    code = ""
    for char in plaintext:
        if char.isupper():
            code += alphabet['capital']
        code += alphabet[char.lower()]
    return code
