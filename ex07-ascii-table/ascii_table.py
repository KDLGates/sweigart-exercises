def print_ASCII_table():
    # ASCII chars are codepoints 32 through 126
    for n in range(32,127):
        print(f'{n} {chr(n)}')
