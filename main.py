def to_uppercase(words):
    """
    Convert each word in the list to uppercase using the map function.
    Args:
    - words (list): List of words to be converted to uppercase.

    Returns:
    - list: List of words in uppercase.
    """
    # Your code here
    return list(map(lambda x: x.upper(), words))


if __name__ == '__main__':
    words = ['apple', 'banana', 'cherry']
    uppercase_list = to_uppercase(words)
    print(uppercase_list)
