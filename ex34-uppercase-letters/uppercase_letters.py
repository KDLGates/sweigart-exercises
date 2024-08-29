import string

def get_uppercase(text: str) -> str:
    """
    Reproduces a string's .upper() method using codepoint addition.
    """
    output = ""
    for char in text:
        if char in string.ascii_lowercase:
            output += chr(ord(char) - (ord('a') - ord('A')))
        else:
            output += char
    return output

assert get_uppercase('Hello') == 'HELLO'
assert get_uppercase('hello') == 'HELLO'
assert get_uppercase('HELLO') == 'HELLO'
assert get_uppercase('Hello, world!') == 'HELLO, WORLD!'
assert get_uppercase('goodbye 123!') == 'GOODBYE 123!'
assert get_uppercase('12345') == '12345'
assert get_uppercase('') == ''
