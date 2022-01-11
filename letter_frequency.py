import string
from collections import Counter


def main():
    with open('alice_encrypted.txt', 'r', encoding='utf-8') as in_file:
        file_content = in_file.read()
    counter = Counter(file_content)
    letter_count = {}
    for letter, count in counter.most_common(1000):
        if letter in string.ascii_letters:
            letter_count[letter] = count

    freq_letters = 'etaonisrhldcumfpgywbkTSAMCINBRPEDHxWLFYGJzjvUqVQXKOZ'
    cipher_key = {}
    for i, letter in enumerate(letter_count):
        cipher_key[letter] = freq_letters[i]

    with open('alice_encrypted.txt', 'r', encoding='utf-8') as in_file:
        for row in in_file:
            for letter in row:
                if letter in cipher_key:
                    print(cipher_key[letter], end='')
                else:
                    print(letter, end='')


if __name__ == '__main__':
    main()
