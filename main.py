#TODO Difficulty selection
#TODO English dictionary, randomly selects word
#TODO Convert this entire project to Wheel of Fortune: Metalhead Edition
#TODO Add ability for user to guess full word
#TODO Add support for compound words

secret_word = list("AVAILABILITY")
secret_word_progress = ["_"] * len(secret_word)
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
guessed = []
max_guesses = 5
game_active = True

print("Welcome to my shitty Hangman game!\n")
print("The " + str(len(secret_word)) + "-letter word has been chosen: " + " ".join(secret_word_progress) + "\n")

while game_active:
    print("Letters Remaining: " + " ".join(alphabet))
    print(f"Guesses Remaining: {max_guesses}")
    print("\nType a letter and press Enter.")

    while True:
        guess = input().upper()
        if guess in guessed:
            print(f"You have already guessed the letter {guess}. Try again.")
        elif len(guess) > 1:
            print("Your guess must be one character at a time. Also, numbers and other characters are currently prohibited. Try again.")
        elif guess == "":
            print("There was no input. Try again.")
        elif guess.isalpha() == False:
            print("Numbers and other characters are currently prohibited. Try again.")
        elif guess.isalpha() and guess not in alphabet:
            print("Your guess is not a possible choice out of the remaining letters. Try again.")
        else:
            break

    instances = 0
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            instances += 1
            secret_word_progress[i] = secret_word[i]
            
    for i in range(len(alphabet)):
        if alphabet[i] == guess:
            alphabet[i] = "_"
            guessed.append(guess)

    if instances < 1:
        max_guesses -= 1
        print(f"\nSorry, the letter {guess} is not in the secret word.\n")
    elif instances == 1:
        print(f"\nThere is one {guess}.")
    else:
       	print(f"\nThere are {instances} {guess}'s!")
        	
    if max_guesses == 0:
        print("You've run out of guesses... R.I.P.\n")
        break
    
    if secret_word_progress == secret_word:
    	print(f"Congratulations! The secret word is: " + "".join(secret_word))
    	break
    else:
    	print("Current progress: " + " ".join(secret_word_progress))
