def rev_sen(sentence):
    # Split string into words (split at spaces in string)
    split_sen = sentence.split()

    # Reverse sentence by reversing list of words
    split_sen.reverse()

    # Join the reversed list of words to form string again, with spaces between words
    # return reversed string
    return " ".join(split_sen)


# Function for getting user input for sentence
def get_sen():

    # Ask user for input and return it
    return input("Enter a sentence: ")


# Main function
def main():
    sen = get_sen()
    result = rev_sen(sen)
    print(result)


# Main
if __name__ == "__main__":
    main()
