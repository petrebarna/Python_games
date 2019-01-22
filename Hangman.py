# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/Petre/Desktop/python/wk3/problems/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    for k in secretWord:
        if k not in lettersGuessed:
            return False

    return True

    # FILL IN YOUR CODE HERE...


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    remainingWord = ''

    for k in secretWord:
        if k in lettersGuessed:
            remainingWord += ' ' + k

        else:
            remainingWord += ' _ '

    return remainingWord


def formatLetters(l):
    return ''.join(l)


def getAvailableLetters(guess, remainingLetters):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    remainingLetters.remove(guess)

    return formatLetters(remainingLetters)


def evaluateGuess(guess, secretWord, lettersGuessed, lives, remainingLetters):

    if guess in lettersGuessed:
        print("Oops! Youve already guessed that letter:" +
              getGuessedWord(secretWord, lettersGuessed))

    elif guess in secretWord:
        lettersGuessed.append(guess)
        getAvailableLetters(guess, remainingLetters)
        print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))

    else:
        lives -= 1
        lettersGuessed.append(guess)
        getAvailableLetters(guess, remainingLetters)
        print("Oops! That letter is not in my word:" +
              getGuessedWord(secretWord, lettersGuessed))

    return lives


def hangman(secretWord):
    

    lengthWord = len(secretWord)

    lettersGuessed = []

    lives = 8

    remainingLetters = list(string.ascii_lowercase)

    print('Welcome to the game, Hangman!')

    print('I am thinking of a word that is ' + str(lengthWord) +
          ' letters long.')

    while isWordGuessed(secretWord, lettersGuessed) is not True:

        if lives > 0:

            print("You have " + str(lives) + " guesses left.")

            print("Available letters: " + formatLetters(remainingLetters))

            guess = input("Please enter a letter: ")

            guessLowerCase = guess.lower()

            lives = evaluateGuess(guessLowerCase, secretWord, lettersGuessed,
                                  lives, remainingLetters)

        else:

            print("Sorry, you ran out of guesses. The word was " + secretWord)
            return None

    print("Congratulations, you won!")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
