import string
import random

def main():
    alphabet = string.ascii_letters
    cipher_alphabet = string.ascii_letters

    cipher_list = []
    for c in cipher_alphabet:
        cipher_list.append(c)

    random.shuffle(cipher_list)
    cipher_alphabet = ''.join(cipher_list)

    with open('alice.txt', 'r', encoding='utf-8') as in_file:
        with open('alice_encrypted.txt', 'w', encoding='utf-8') as out_file:
            for line in in_file:
                for letter in line:
                    if letter in alphabet:
                        idx = alphabet.index(letter)
                        cipher_letter = cipher_alphabet[idx]
                        out_file.write(cipher_letter)
                    else:
                        out_file.write(letter)


if __name__ == '__main__':
    main()
