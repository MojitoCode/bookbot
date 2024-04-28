def main():
    book_path = "./books/frankenstein.txt" 
    with open(book_path) as f:
        file_contents = f.read()
    
    words = file_contents.split()
    num_of_words = len(words)
    print(f"There were {num_of_words} words found in the: {book_path} document.")

main()
