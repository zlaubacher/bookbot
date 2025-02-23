def word_count(contents):
    #sets up a list called total_words with each individual word from the book passed into the function
    total_words = contents.split()
    #counts up the length of the list in order to establish a word count
    num_words = len(total_words)
    return num_words

def character_frequency(contents):
    #establishes a dictionary which will eventually contain key value pairs of a letter and the number of times that letter appears in the document
    characters_contained = {}
    #converts every letter to lower case so that we're counting each letter rather than splitting the frequencies into upper and lower case as well
    letters = contents.lower()
    #establishes a loop to cycle through every character in the provided text
    for letter in letters:
        #If the current character is not in the dictionary, add the letter as a key and set its value to 1, to show the first time that character has appeared in the text.
        if letter not in characters_contained:
            characters_contained[letter] = 1
        #If the character IS in the dictionary already, increment its value by 1.
        else:
            characters_contained[letter] += 1
    return characters_contained