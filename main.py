import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def print_report(sorted_letters, words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("-------- Character Count -------")
    for item in sorted_letters:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")


def main():
    from stats import word_count
    from stats import char_count
    from stats import sorted_char_count
    print("Usage: python3 main.py <path_to_book>")
    txt = get_book_text(sys.argv[1])
    words = word_count(txt)
    letters = char_count(txt)
    sorted_letters = sorted_char_count(txt)
    
    print_report(sorted_letters, words)
    print(sys.argv)
main()
