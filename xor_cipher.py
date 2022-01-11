def main():
    clear_letter = 'H'
    key_letter = 'S'
    # Encrypt
    clear_value = ord(clear_letter)
    key_value = ord(key_letter)
    cipher_value = clear_value ^ key_value

    # Decrypt
    clear_value = key_value ^ cipher_value
    print(chr(clear_value))



if __name__ == '__main__':
    main()
