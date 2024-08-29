def print_upper_words(word_list, must_start_with):
    """For a list of words, prints out each word on a separate line that starts with a certain letter, in all uppercase."""

    # Iterate over wordlist
    for word in word_list:
        # Check to see if the first letter in the word is on of the letter it needs to start with
        if word[0].lower() in must_start_with:
            # Print the word in uppercase
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})

