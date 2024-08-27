def convert_strings_to_integers(s: str) -> int:
    """
    Reproduces int(s), converting a string to an integer.
    """
    result = 0
    sign = 1

    if s[0] == '-':
        sign = -1
        s = s[1:]
    
    for chr in s:
        # Convert chr to its numeric value
        val = ord(chr) - ord('0')
        # Update result based on this value and its place
        result = result * 10 + val
    
    return result * sign

for i in range(-10000, 10000):
    assert convert_strings_to_integers(str(i)) == int(str(i))
