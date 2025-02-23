def get_book_text(location):
    #opens the file within the location to be specified once the function is called and accesses its contents in a variable called book
    with open(location) as book:
        #reads the contents of the file as a text string
        contents = book.read()
        return contents

from stats import word_count

from stats import character_frequency

from stats import sort_frequencies

def main():
    #defines the file path for the book to be read and creates it as a variable
    location = "./books/frankenstein.txt"
    #runs the get_book_text function to read the text of the book given to it by the location variable and passes its text into the contents variable
    contents = get_book_text(location)
    #runs the word_count function, which sets up a list of all individual words in the document and then returns that list's length
    num_words = word_count(contents)
    num_characters = character_frequency(contents)
    #runs a trio of functions that takes the num_characters dictionary and splits it into a list of dictionaries, then sorts from highest frequency of appearance to lowest.
    sorted_characters = sort_frequencies(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {location}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_characters:
        for char in char_dict:
            if char.isalpha():
                print(f"{char}: {char_dict[char]}")
    print("============= END ===============")

main()