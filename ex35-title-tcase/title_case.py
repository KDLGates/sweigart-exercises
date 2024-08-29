import string

def get_title_case(text: str) -> str:
    """
    Reproduces String's .title() method for converting
    input text to Title Case.
    """
    if not text:
        return ''
    
    result = [text[0].upper()]
    for i in range (1, len(text)):
        if text[i-1] in string.whitespace + string.punctuation + string.digits:
            result.append(text[i].upper())
        else:
            result.append(text[i].lower())
    return ''.join(result)


assert get_title_case('Hello, world!') == 'Hello, World!'
assert get_title_case('HELLO') == 'Hello'
assert get_title_case('hello') == 'Hello'
assert get_title_case('hElLo') == 'Hello'
assert get_title_case('') == ''
assert get_title_case('abc123xyz') == 'Abc123Xyz'
assert get_title_case('cat dog RAT') == 'Cat Dog Rat'
assert get_title_case('cat,dog,RAT') == 'Cat,Dog,Rat'

import random

random.seed(42)
chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')
for i in range(1000):
    random.shuffle(chars)
    assert get_title_case(''.join(chars)) == ''.join(chars).title()
