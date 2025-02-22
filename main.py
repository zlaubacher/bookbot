def get_book_text(location):
    #opens the file within the location to be specified once the function is called and accesses its contents in a variable called book
    with open(location) as book:
        #reads the contents of the file as a text string
        contents = book.read()
        return contents

from stats import word_count

def main():
    #defines the file path for the book to be read and creates it as a variable
    location = "./books/frankenstein.txt"
    #runs the get_book_text function to read the text of the book given to it by the location variable and passes its text into the contents variable
    contents = get_book_text(location)
    #runs the word_count function, which sets up a list of all individual words in the document and then returns that list's length
    num_words = word_count(contents)
    print(f"{num_words} words found in the document")

main()