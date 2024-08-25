import string, random

def generate_password(chars: int) -> str:
    """
    Generates a password with special rules per the exercise description.
    """
    if chars < 12:
        chars = 12
    
    password = ""
    for char in range(chars):
        match char % 4:
            case 0:
                password += random.choice(string.ascii_lowercase)
            case 1:
                password += random.choice(string.ascii_uppercase)
            case 2:
                password += random.choice(string.digits)
            case 3:
                password += random.choice('~!@#$%^&*()_+')
    return password
