def reverse_string(text: str) -> str:
    """
    Reverses a string using a list cast.
    """
    if not text:
        return ''
    l = list(text)
    output = []
    for chr in range(len(l)):
        output.append(l.pop())
    output = ''.join(output)
    return output

assert reverse_string('Hello') == 'olleH'
assert reverse_string('') == ''
assert reverse_string('aaazzz') == 'zzzaaa'
assert reverse_string('xxxx') == 'xxxx'
