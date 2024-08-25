def fizz_buzz(upto):
    """
    Iterates over the range from 1 to a number given and prints the number\
    unless the conditions for Fizz, Buzz or FizzBuzz are met.\
    """
    for n in range(1, upto + 1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz ", end='')
        elif n % 3 == 0:
            print("Fizz ", end='')
        elif n % 5 == 0:
            print("Buzz ", end='')
        else:
            print(f'{n} ', end='')

fizz_buzz(100)