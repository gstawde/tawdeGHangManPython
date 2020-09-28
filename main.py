# import Random functions
import random

# Hang Man Game!!

# The first step is for the computer to pick a word but dont tell the word to player
words = ["immaculate","minor","dancing","conquer","magnificent","twilight","comparitively","sharpened","intrinsic","unbelievable"]

# pick a random word from our list called words
randomInt = random.randint(0, len(words) - 1)
# create a String to hold the correct word
correctWord = words[randomInt]
# create a list to store their guesses
guesses = []
# create a String with blank spaces for them to see how long the word is --> e.g. _ _ _ _ _
blanks = []
for i in range(0, len(correctWord)):
    blanks.append("_")


# Set the amount of lives to 12
livesLeft = 7
# Open the game (Welcome to hangman + explain the rules)
print("Welcome to Hangman!!\n")
# How to play:
print("Here is how to play:")
print("You will have" + str(livesLeft) + "lives in total.")
print("1. Guess a letter and the computer will tell you if the letter is in the answer.")
print("2. Whenever you guess incorrectly you lose a life.")
print("3. Duplicate guesses -- incorrect or not -- will have no impact on your lives left. However, they are invalid guesses so avoid them.")
print("4. If you run out of lives before guessing the whole word, then GAME OVER.")
print("\nLet's Start!\n")

hasWon = False
# game starts
while (livesLeft > 0):
    # Have the computer tell the player to type in a letter
    print("Here is the word so far: " + str(blanks))
    userInput = str(input("Guess a letter: "))
    # Check if it matches any of the letters in the word
    # If they guess the same letter, don't lose a life, but ask to try again
    if guesses.__contains__(userInput) :
       print("\nHey you already guessed that one! Try something else :)\n") 
    else :
        # If the letter is incorrect then it will be on the board -- lose a life; print "Answer is incorrect"
        if userInput not in correctWord:
            print("\nYour guess is incorrect!\n")
            guesses.append(userInput)
            livesLeft = livesLeft - 1
        # If correct, print "You are correct!" -- fill in those letters
        else:
            print("\nYour guess is correct!\n") 
            guesses.append(userInput)
            for i in range(0,len(blanks)):
                if correctWord[i] == userInput:
                    blanks[i] = userInput
    # Check if word is complete
    if not (blanks.__contains__("_")):
        hasWon = True
        break;

if (hasWon) :
    print("\nGreat job you guessed the word!\nThe correct answer was: " + correctWord)
else :
    print("\nSorry, but you lost!\nThe correct word was: " + correctWord + "\nBetter luck next time!! :)")      
