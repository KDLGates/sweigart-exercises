def write_to_file(path, text):
    """
    Writes given text to file, overwriting.
    """
    with open(path, 'w', encoding='UTF-8') as f:
        f.write(text)

def append_to_file(path, text):
    """
    Writes given text to file, appending.
    """
    with open(path, 'a', encoding='UTF-8') as f:
        f.write(text)

def read_from_file(path):
    """
    Prints string of content from a text file.
    """
    with open(path, 'r', encoding='UTF-8') as f:
        return f.read()

write_to_file('greet.txt', 'Hello!\n')
append_to_file('greet.txt', 'Goodbye!\n')
assert read_from_file('greet.txt') == 'Hello!\nGoodbye!\n'
