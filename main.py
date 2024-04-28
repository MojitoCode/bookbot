def main():
    book_path = "./books/frankenstein.txt" 
    with open(book_path) as f:
        file_contents = f.read()
    
    words = file_contents.split()
    num_of_words = len(words)
    print(f"There were {num_of_words} words found in the: {book_path} document.")

def count_letters():
    book_chars = {}
    book_path = "./books/frankenstein.txt" 
    with open(book_path) as f:
        for i in f:
            lower_string = i.lower()
            if lower_string in book_chars:
                book_chars[lower_string] +=1
            else:
                book_chars[lower_string] = 1
    print(lower_string)

main()
count_letters()
