import sys
from stats import count_words, char_amount_in_text, sort_dic_and_counts


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    counts = char_amount_in_text(book_text)
    sorted_counts = sort_dic_and_counts(counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------") 
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    print(f"{counts}")

    for entry in sorted_counts:
        ch = entry["char"]
        if ch.isalpha():
            print(f"{ch}: {entry['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
    