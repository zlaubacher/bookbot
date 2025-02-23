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

def sort_on(dict):
    #when given a dictionary, it looks at each value from the key value pair and returns only that value (allowing for sorting by frequency later)
    for char in dict:
        return dict[char]

def list_of_frequencies(characters_contained):
    #establishes a list to be populated by dictionaries of single key/value pairs to enable sorting.
    list_of_characters = []
    #loops through a dictionary and creates a list of new single key/value pairs.
    for character in characters_contained:
        sorted_pair = {character: characters_contained[character]}
        list_of_characters.append(sorted_pair)
    return list_of_characters

def sort_frequencies(characters_contained):
    #runs the list_of_frequencies function in order to generate the list of single key/value pairs
    character_list = list_of_frequencies(characters_contained)
    #sorts that list in order from highest frequency to lowest frequency
    character_list.sort(reverse = True, key=sort_on)
    return character_list