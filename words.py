def print_upper_words(words, char_set):
    """Print out each word in a list that has been picked by a set of characters, on a separate line, but in all uppercase.
        For Example:

            print_upper_words(["hello", "hey", "goodbye","yo", "yes"])

        Should Print:

        HI
        HELLO
        COW
    """

    for word in words:
        for char in char_set:
            if word.startswith(char):
                print(word.upper())
        else:
            continue


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {"h", "y"})
