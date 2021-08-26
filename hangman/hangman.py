import sys
import random
import argparse
import os

guessedLetters = []
wrongLetters = []

def validStartInput(input):
    try:
        if (input == "y" or input == "n"):
            return True
        else:
            print("Invalid Input")
            return False
    except:
        print("Invalid Input")
        return False

def validDifficulty(input):
    try:
        if (input == "e" or input == "m" or input == "h"):
            return True
        else:
            print("Invalid Difficulty")
            return False
    except:
        print("Invalid Difficulty")
        return False

def validLetter(input: str):
    try:
        if input.isalpha() and len(input) == 1:
            return True
        else:
            print("Please Input one Letter")
            return False
    except:
        print("Please Input one Letter")
        return False

def setDiff(diff):
    if diff == "e":
        return 0
    elif diff == "m":
        return 1
    elif diff == "h":
        return 2
    else:
        return -1

def printHangman(difficulty, errs):
    print('   -------------')
    print('   |           |')
    if errs == 0:
        print('               |')
        print('               |')
        print('               |')
        print('             -----')
        return
    elif errs > 0:
        print('   O           |')

    if errs == 2:
        print('   |           |')
        print('               |')
    elif errs < 2:
        print('               |')
        print('               |')

    if difficulty > 0:
        if errs == 3:
            print('  /|\          |')
            print('               |')
        if errs == 4:
            print('  /|\          |')
            print('  / \          |')
    elif difficulty == 0:
        if errs == 3:
            print('  /|           |')
            print('               |')
        elif errs > 3:
            print('  /|\          |')
        if errs == 5:
            print('  /            |')
        elif errs > 5:
            print('  / \          |')
        elif errs == 4:
            print('               |')

    print('             -----')

def printWrong(difficulty):
    if difficulty < 2:
        print("Wrong Letters:", end=" ")
        for letter in wrongLetters:
            print(letter, end=" ")
        print("")

def printWord(word: str, correct):
    index = 0
    print("     ", end=" ")
    for val in correct:
        if val == 1:
            print(word[index].upper(), end=" ")
        else:
            if word[index].isalpha():
                print("_", end=" ")
            else:
                print(word[index], end=" ")
        index += 1
    print("")

def updateWord(word: str, correct, letter: str):
    match = False
    index = 0
    for lett in word:
        if lett.lower() == letter.lower():
            correct[index] = 1
            match = True
        index += 1
    
    guessedLetters.append(letter)
    if not match:
        wrongLetters.append(letter)
        return False
    
    return True

def startGame(word: str, correct):
    print("Difficulties:")
    print("Easy: 6 lives, Medium: 4 Lives, Hard: 4 Lives, No Letter Bank")
    val_in = input("What difficulty would you like to play? [E/M/H]: ").lower()
    while not validDifficulty(val_in):
        val_in = input("What difficulty would you like to play? [E/M/H]: ").lower()
    diff = setDiff(val_in)
    wrongNum = 0
    game_on = True
    complete = False
    while game_on:
        printHangman(diff, wrongNum)
        printWord(word, correct)
        printWrong(diff)

        inp = input("Your Guess: ").lower()
        while not validLetter(inp):
            inp = input("Your Guess: ").lower()
        
        if inp in guessedLetters:
            print("Unlucky! You already guessed that!")
            wrongNum += 1
        elif not updateWord(word, correct, inp):
            wrongNum += 1

        if diff > 0 and wrongNum == 4:
            game_on = False
        elif diff == 0 and wrongNum == 6:
            game_on = False
        elif finishedWord(word, correct):
            game_on = False
            complete = True

    printHangman(diff, wrongNum)
    printWord(word, correct)
    if complete:
        print("Congratulations you completed the word!")
    else:
        print("Uh-Oh, you couldn't complete the word.")
        print("The word was {}.".format(word.upper()))

def finishedWord(word: str, correct):
    index = 0
    for val in correct:
        if val == 0:
            if word[index].isalpha():
                return False

        index += 1
    
    return True

def leaveGame():
    print("Thanks for playing. See you next time. (^.^)/")
    sys.exit(0)

parser = argparse.ArgumentParser(description="Play Hangman")
parser.add_argument('-f', metavar='f', type=str, default='default.txt', help="file with all usable words (default: default.txt)")
args = parser.parse_args()
if not os.path.isfile(args.f):
    print('ERROR: File provided does not exist!')
    sys.exit()

words = []
with open(args.f, 'r') as f:
    for l in f:
        words.append(l.strip())

if len(words) == 0:
    print('ERROR: File has no words in it!')
    sys.exit()

print("Welcome to Hangman!")

while(1):
    val_in = input("Would you like to play? [Y/N]: ")
    while not validStartInput(val_in.lower()):
        val_in = input("Would you like to play? [Y/N]: ")

    if val_in.lower() == "y":
        wrongLetters.clear()
        guessedLetters.clear()
        word = random.choice(words)
        correct = []
        for letter in word:
            correct.append(0)
        startGame(word, correct)
    elif val_in.lower() == "n":
        leaveGame()
    else:
        print("Something very bad happened.")
        leaveGame()
