import string

def rot13(text: str) -> str:
    """
    Applies the ROT 13 cypher to text.
    That is, 'rotates' (advances) alphanumerics within the alphabet 13 characters.
    """

    # We'll use string's translation tables.
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    lower_trans = str.maketrans(lower, lower[13:] + lower[:13])
    upper_trans = str.maketrans(upper, upper[13:] + upper[:13])
    trans = {**lower_trans, **upper_trans}
    
    return text.translate(trans)


assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'
