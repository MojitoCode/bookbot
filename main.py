book_path = "./books/frankenstein.txt"
book_title = book_path[8:]
def main(): 
    with open(book_path) as f:
        file_contents = f.read()
    
    words = file_contents.split()
    num_of_words = len(words)
    print(f"There were {num_of_words} words found in the: {book_title} document.")

def sort_dict(char_list):
    return char_list["occurence"]

def count_letters():
    book_chars = {} 

    with open(book_path) as f:
        book = f.read()

    for char in book:
        if char.isalpha():
            #convert the line to lower
            lower_string = char.lower()
            if char in book_chars:
                book_chars[char] +=1
            else:
                book_chars[char] = 1

    char_list = [{"character": char, "occurence": number} for char, number in book_chars.items()]
    char_list.sort(reverse=True, key=sort_dict)

    return char_list, book_path

def print_report():
    char_list, book_path = count_letters()

    print(f"--- Begin Report of {book_title} ---")
    main()

    for i in char_list:
        print(f"The {i['character']} character was found {i['occurence']}")
    print(f"--- End Report ---")

print_report()