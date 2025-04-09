from stats import get_num_words
from stats import characters
from stats import sort_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    word_count = get_num_words(book_text)
    char_count = characters(book_text)
    sorted_list = sort_characters(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

main()