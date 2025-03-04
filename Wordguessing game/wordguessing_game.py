import random

name = input("What is your name? ")

print("Good Luck ! ", name)

words = ['ryukendo', 'calculus', 'erenyeager', 'naruto', 'sasuke', 'vegeta', 'gohan', 'trunks', 'gohan', 'goku',
         'python', 'mathematics', 'messi', 'ronaldo',
         'coriolis', 'water', 'neural', 'geeko',]

word = random.choice(words)                        #The program selects a random word from the list of words using random.choice() function.

print("Guess the characters")
 
guesses = ''                                       #It holds the characters that the player guesses.
turns = 12                                         #The number of turns the player has to guess the word. intially 12

while turns > 0:

    failed = 0                                     #A counter for the number of characters that have not been correctly guessed

    for char in word:                              #The for loop iterates through each character in the word

        if char in guesses:
            print(char, end=" ")

        else:
            print("_")                              # if the character has not been guessed, _ is displayed, and failed attempt increases by 1
            failed += 1

    if failed == 0:                                #it mean all characters in the word have been correctly guessed and the user wins the game and correct word is displayed and the game end with the break statemnet
        print("You Win")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character:")            #The player is asked to guess a character

    guesses += guess

    if guess not in word:                          #If the character guessed by the player is not in the word, the number of turns is reduced by 1 an wrong messege is displayed

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:                              # If the user runs out of the turns, the game ends and it diaplys You lose 
            print("You Loose")

