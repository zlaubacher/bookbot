def word_count(contents):
    #sets up a list called total_words with each individual word from the book passed into the function
    total_words = contents.split()
    #counts up the length of the list in order to establish a word count
    num_words = len(total_words)
    return num_words