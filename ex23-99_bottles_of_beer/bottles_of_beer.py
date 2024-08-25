def print_song() -> None:
    for n in reversed(range(1, 100)):
        print(f'{n} {'bottles' if n > 1 else 'bottle'} of beer on the wall,')
        print(f'{n} {'bottles' if n > 1 else 'bottle'} of beer,')
        print(f'Take one down,')
        print(f'Pass it around,')
        if n > 1:
            print(f'{n-1} bottles of beer on the wall,')
            print()
        else:
            print('No more bottles of beer on the wall!')
