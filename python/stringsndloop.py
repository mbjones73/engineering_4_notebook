def splitCharacters(word): # Returns a list with each character from the word passed to it
    return list(word)

userInput = input("Type in your word or sentence, then press enter:") # Asks for and records the sentence input by the user


for word in userInput.split():
    for character in splitCharacters(word):
        print(character)
    print("-")
