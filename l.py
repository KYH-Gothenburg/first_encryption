import string
from collections import Counter


def main():
    with open('alice_encrypted.txt', 'r', encoding='utf-8') as in_file:
        file_content = in_file.read()
    counter = Counter(file_content)
    c = {letter: count for letter, count in counter.most_common(10000) if letter in string.ascii_letters}
    print(c)


if __name__ == '__main__':
    main()
