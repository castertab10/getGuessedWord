def getGuessedWord():
    
    secretWord = input("Input the secret word: ")
    lettersGuessed = input("Input a list of letters: ")
    n = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            n = n + letter
        else:
           n = n + '_ '
    return n