
        if char in guesses:
            print(char, end=" ")

        else:
            print("_")                              # if the character has not been guessed, _ is displayed, and failed attempt increases by 1
            failed += 1

    if failed == 0:                                #it mean all characters in the word have been correctly guessed and the user wins the game and correct word is displayed and the game end with the break statemnet
        print("You Win")
        print("The word is: ", word)