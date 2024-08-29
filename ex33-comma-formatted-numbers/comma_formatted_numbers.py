def comma_format(number: float) -> str:
    """
    Takes a US/UK styled float with optional decimal part,
    then returns its string representation with commas.
    """
    s = str(number)
    decimal_part = ""
    decimal_index = s.find('.')
    
    if decimal_index != -1:
        decimal_part = s[decimal_index:]
        integer_part = s[:decimal_index]
    else:
        integer_part = s
    
    # Reverse the integer part to insert commas every three digits
    reversed_integer = integer_part[::-1]
    output_integer_part = ','.join(reversed_integer[i:i+3] for i in range(0, len(reversed_integer), 3))
    
    # Reverse it back to the original order
    output_integer_part = output_integer_part[::-1]
    
    return output_integer_part + decimal_part

assert comma_format(1) == '1'
assert comma_format(10) == '10'
assert comma_format(100) == '100'
assert comma_format(1000) == '1,000'
assert comma_format(10000) == '10,000'
assert comma_format(100000) == '100,000'
assert comma_format(1000000) == '1,000,000'
assert comma_format(1234567890) == '1,234,567,890'
assert comma_format(1000.123456) == '1,000.123456'
