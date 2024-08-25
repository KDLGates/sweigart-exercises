def find_and_replace(text: str, old_text: str, new_text: str) -> str:
    try:
        idx = text.index(old_text)
        return text[:idx] + new_text + find_and_replace(text[idx + len(new_text):], old_text, new_text)
    except ValueError:
        return text

assert find_and_replace('The fox', 'fox', 'dog') == 'The dog'
assert find_and_replace('fox', 'fox', 'dog') == 'dog'
assert find_and_replace('Firefox', 'fox', 'dog') == 'Firedog'
assert find_and_replace('foxfox', 'fox', 'dog') == 'dogdog'
assert find_and_replace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
