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
            #convert the line to lower
            lower_string = i.lower()
            for l in lower_string:
                if l in book_chars:
                    book_chars[l] +=1
                else:
                    book_chars[l] = 1
    return book_chars

main()
result = count_letters()
print(result)