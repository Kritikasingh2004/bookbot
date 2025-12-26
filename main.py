import sys
from stats import book_word_count, book_letter_count, letter_count_sort

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path= sys.argv[1]
    book = get_book_text(book_path)
    num_words = book_word_count(book)
    letter_count = book_letter_count(book)
    character_count = letter_count_sort(letter_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for c in character_count:
        if c['char'].isalpha():
            print(f"{c['char']}: {c['num']}")
        


main ()
