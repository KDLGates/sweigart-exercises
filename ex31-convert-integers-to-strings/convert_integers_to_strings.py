def convert_int_to_str(integer_num: int) -> str:
    """
    Replicates str() for integer_num in [-10000, 10000].
    """
    result = ""
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if integer_num < 0:
        result += "-"
        if integer_num != -10000:
            integer_num = -integer_num
    reversed = ""
    match integer_num:
        case n if integer_num == -10000:
            reversed = '00001'
        case n if integer_num > -10 and integer_num < 10:
            reversed += digits[n % 10]
        case n if integer_num > -100 and integer_num < 100:
            for i in range(2):
                reversed += digits[integer_num % 10]
                integer_num //= 10
        case n if integer_num > -1000 and integer_num < 1000:
            for i in range(3):
                reversed += digits[integer_num % 10]
                integer_num //= 10
        case n if integer_num > -10000 and integer_num < 10000:
            for i in range(4):
                reversed += digits[integer_num % 10]
                integer_num //= 10
        case _:
            raise ValueError('Number out of range [-10000, 10000]')
    return result + reversed[::-1]

for i in range(-10000, 10000):
    assert convert_int_to_str(i) == str(i)
