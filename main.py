from stats import get_num_words, get_characters_count_dict

def main():
    print("============ BOOKBOT ============")
    frankenstein_relative_path = "books/frankenstein.txt"
    print(f"Analyzing book found at {frankenstein_relative_path}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(filepath=frankenstein_relative_path)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count_dict = get_characters_count_dict(frankenstein_relative_path)
    for key in char_count_dict.keys():
        print(f"{key}: {char_count_dict[key]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()