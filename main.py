import sys
from stats import count_words, count_characters, sorted_list

def get_book_text(filepath): 
    try:
        with open(filepath) as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        print("book not found at specified location")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    book_text = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    count_words(book_text)
    print("--------- Character Count -------")
    character_count = count_characters(book_text) # dictionary of letters and counts e.g. 't': 29493
    s_list = sorted_list(character_count)
    for i in s_list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()