from stats import get_num_words, get_characters_count_dict
import sys

def main(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    num_words = get_num_words(filepath=book_path)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_count_dict = get_characters_count_dict(book_path)
    for key in char_count_dict.keys():
        print(f"{key}: {char_count_dict[key]}")
    print("============= END ===============")

if __name__ == "__main__":
    if (len(sys.argv)) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    main(book_path)