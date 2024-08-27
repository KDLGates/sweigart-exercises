import itertools

def print_handshakes(people) -> int:
    """
    Prints all unique handshakes (combinations) from a list of people's names.
    """
    pairs = list(itertools.combinations(people, 2))
    for pair in pairs:
        print(f'{pair[0]} shakes hands with {pair[1]}')
    return len(pairs)

assert print_handshakes(['Alice', 'Bob']) == 1
assert print_handshakes(['Alice', 'Bob', 'Carol']) == 3
assert print_handshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
