from stats import get_num_words
from stats import count_characters
from stats import sort_character_dictionary
import sys

def get_book_text(book):
    """
    Extracts the text from a book object.

    Args:
        book: The book object to extract text from.

    Returns:
        str: The extracted text.
    """
    print(f"Extracting text from {book}")
    with open(book) as f:
        file_contents = f.read()        
    return file_contents

def main():
    """
    Main function to execute the script.
    """
    print("Starting the script...")
    if len(sys.argv) > 1:
        book = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(book)
    num_words = get_num_words(text)
    character_count = count_characters(text)
    sorted_dictionary = sort_character_dictionary(character_count) 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count -----------")
    for char in sorted_dictionary:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


main()


