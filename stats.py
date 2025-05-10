def get_num_words(text):
    """
    Counts the number of words in a given text.

    Args:
        text: The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    print("Counting words...")
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Counts the number of characters in a given text.

    Args:
        text: The text to count characters in.

    Returns:
        dictionary: The number of characters in the text.
    """
    print("Counting characters...")
    char_count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]


def sort_character_dictionary(char_count):
    """
    Sorts a character dictionary by character.

    Args:
        char_count: The character dictionary to sort.

    Returns:
        list: A sorted list of tuples (character, count).
    """
    print("Sorting character dictionary...")
    sorted_list = []
    for char in char_count:
        if not char.isalpha():
            continue
        entry = {}
        entry["char"] = char
        entry["num"] = char_count[char]
        sorted_list.append(entry)
    sorted_list.sort(reverse = True, key=sort_on)
    return sorted_list
