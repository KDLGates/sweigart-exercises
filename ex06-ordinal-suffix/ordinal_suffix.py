def ordinal_suffix(n):
    """
    Returns the string representation of a number with the English ordinal suffix.
    e.g., 1st, 2nd, 3rd, 4th, ...
    """
    n = str(n)
    if int(n) > 10 and int(n) < 19:
        # teen numbers are a special case all ending -th
        return n + 'th'
    if n[-1] == '1':
        return n + 'st'
    elif n[-1] == '2':
        return n + 'nd'
    elif n[-1] == '3':
        return n + 'rd'
    else:
        return n + 'th'

assert ordinal_suffix(0) == '0th'
assert ordinal_suffix(1) == '1st'
assert ordinal_suffix(2) == '2nd'
assert ordinal_suffix(3) == '3rd'
assert ordinal_suffix(4) == '4th'
assert ordinal_suffix(10) == '10th'
assert ordinal_suffix(11) == '11th'
assert ordinal_suffix(12) == '12th'
assert ordinal_suffix(13) == '13th'
assert ordinal_suffix(14) == '14th'
assert ordinal_suffix(101) == '101st'

def append_ordinal_suffix_using_modulo(n):
    if n % 100 in (11, 12, 13):
        return str(n) + 'th'
    elif n % 10 == 1:
        return str(n) + 'st'
    elif n % 10 == 2:
        return str(n) + 'nd'
    elif n % 10 == 3:
        return str(n) + 'rd'
    else:
        return str(n) + 'th'

assert append_ordinal_suffix_using_modulo(0) == '0th'
assert append_ordinal_suffix_using_modulo(1) == '1st'
assert append_ordinal_suffix_using_modulo(2) == '2nd'
assert append_ordinal_suffix_using_modulo(3) == '3rd'
assert append_ordinal_suffix_using_modulo(4) == '4th'
assert append_ordinal_suffix_using_modulo(10) == '10th'
assert append_ordinal_suffix_using_modulo(11) == '11th'
assert append_ordinal_suffix_using_modulo(12) == '12th'
assert append_ordinal_suffix_using_modulo(13) == '13th'
assert append_ordinal_suffix_using_modulo(14) == '14th'
assert append_ordinal_suffix_using_modulo(101) == '101st'
