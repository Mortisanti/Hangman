#TODO Difficulty selection
#TODO English dictionary, randomly selects word
#TODO Convert this entire project to Wheel of Fortune: Metalhead Edition

secret_word = list("TESTWORD")
secret_word_progress_before = ["_"] * len(secret_word)
secret_word_progress_after = ["_"] * len(secret_word)
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
max_guesses = 6
game_active = True

print("Welcome to my shitty Hangman game!\n")
print("The " + str(len(secret_word)) + "-letter word has been chosen: " + " ".join(secret_word_progress_before) + "\n")

while game_active:
    print("Letters left: " + " ".join(alphabet))
    print(f"Guesses left: {max_guesses}")
    print("\nType a letter and press Enter.")
    guess = input().upper()
    
    while len(guess) != 1 or guess not in alphabet:
        print("Invalid input. Try again")
        guess = input().upper()
    
    instances = 0
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            instances += 1
            secret_word_progress_after[i] = secret_word[i]
            
    for i in range(len(alphabet)):
	    if alphabet[i] == guess:
	        alphabet[i] = "_"

    if secret_word_progress_before == secret_word_progress_after:
        max_guesses -= 1
        print(f"\nSorry, the letter {guess} is not in the secret word.\n")
    else:
        secret_word_progress_before = secret_word_progress_after
        if instances == 1:
        	print(f"\nThere is one {guess}.")
        else:
        	print(f"\nThere are {instances} {guess}'s!")
        	
    if max_guesses == 0:
        print("You've run out of guesses... R.I.P.")
        break
    
    if secret_word_progress_after == secret_word:
    	print(f"Congratulations! The secret word is: " + "".join(secret_word))
    	break
    else:
    	print("Current progress: " + " ".join(secret_word_progress_after))
