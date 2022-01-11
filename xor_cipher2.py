def main():
    message = 'This is my top secret message. Hide it well.'
    key = 's3cr37'

    for i, letter in enumerate(message):
        key_index = i % len(key)
        print(f'{letter} will be encrypted with {key[key_index]}')



if __name__ == '__main__':
    main()
