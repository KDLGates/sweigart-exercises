def print_song() -> None:
    for n in reversed(range(1, 100)):
        bottle_word = 'bottles' if n > 1 else 'bottle'
        print(f'{n} {bottle_word} of beer on the wall,')
        print(f'{n} {bottle_word} of beer,')
        print('Take one down,')
        print('Pass it around,')
        if n > 1:
            print(f'{n-1} bottles of beer on the wall,')
            print()
        else:
            print('No more bottles of beer on the wall!')
