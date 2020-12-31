#TODO Incorporate Tkinkter or PyQt5 GUI
#TODO Create web app version using Flask?
#TODO Add ability for user to guess full word
#TODO Add support for compound words and words with spaces
#TODO Save file with list of words that the user won/lost
#TODO Hints?

import random

# Default game settings, not including difficulty
def initialize_settings():
    playing = True
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    guessed = []
    max_guesses = 5
    return playing, alphabet, guessed, max_guesses

# Ask the user to choose a difficulty, which just determines which file/word lengths to use
def choose_difficulty():
    while True:
        difficulty_chosen = input("> ").upper()
        if difficulty_chosen == 'EASY' or difficulty_chosen == 'MEDIUM' or difficulty_chosen == 'HARD':
            break
        else:
            print("Invalid input. Try again.")
    return difficulty_chosen

# Open the respective file for the difficulty chosen, read the data, and create a Python list with each word as an element
def generate_wordlist():
    with open(f'{difficulty}.txt', 'r') as f:
        words = f.read()
        wordlist = words.splitlines()
    return wordlist

# Choose a random word from the list that was created after the difficulty was chosen
# Store it in a variable and create an "empty" word matching the length of the secret word
def set_secret_word():
    word_selection = random.randint(1, len(wordlist))
    secret_word = list(wordlist[word_selection].upper())
    secret_word_string = wordlist[word_selection].upper()
    secret_word_length = str(len(secret_word))
    secret_word_progress = ["_"] * len(secret_word)
    return secret_word, secret_word_string, secret_word_length, secret_word_progress

# Show the user which letters they've guessed correctly (if any), which letters of the alphabet remain, and how many guesses they have left
def show_status():
    current_progress = " ".join(secret_word_progress)
    letters_remaining = " ".join(alphabet)
    print(f"Current progress: {current_progress}")
    print(f"Letters Remaining: {letters_remaining}")
    print(f"Guesses Remaining: {max_guesses}")

# Strenuously check the user's input for validity
# This could have been a catch-all, but I wanted some specific, varied responses
def get_guess():
    while True:
        guess = input("Your input: ").upper()
        if guess == 'ATTEMPT':
            print("\nBE CAREFUL! You have chosen to guess the full word. If your input is wrong, or you make a typo, you lose all of your guesses.")
            print("Are you sure you want to continue? YES | NO")
            while True:
                proceed = input("> ").upper()
                if proceed == 'Y' or proceed == 'YES':
                    attempt = True
                    break
                elif proceed == 'N' or proceed == 'NO':
                    attempt = False
                    break
                else:
                    print("Invalid input.")
            if attempt == True:
                break
            else:
                continue
        else:
            if guess in guessed:
                print(f"You have already guessed the letter {guess}. Try again.")
            elif len(guess) > 1:
                print("Your guess must be one character at a time, or the word 'ATTEMPT'. Also, numbers and other characters are currently prohibited. Try again.")
            elif guess == "":
                print("There was no input. Try again.")
            elif guess.isalpha() == False:
                print("Numbers and other characters are currently prohibited. Try again.")
            elif guess.isalpha() and guess not in alphabet:
                print("Your guess is not a possible choice out of the remaining letters. Try again.")
            else:
                break
    return guess

# Attempt full word guess
# UNDER CONSTRUCTION
def attempt_full_word():
    accident = 0
    while True:
        guess = input("> ").upper()
        if guess == secret_word_string:
            correct = True
            break
        elif guess == "":
            print("There was no input. Try again.")
        elif guess.isalpha() == False:
            print("Numbers and other characters are currently prohibited. Try again.")
        elif len(guess) != len(secret_word_string) and accident == 0:
            accident += 1
            print("Word length does not match. You get a second chance. Try one more time.")
        else:
            correct = False
            break
    return correct


# Count each instance of the guessed letter that exists in the secret word and replace the empty spots of the progress word, if a correct guess
def check_letter_instances():
    instances = 0
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            instances += 1
            secret_word_progress[i] = secret_word[i]
    return instances

# Remove the guessed letter from the alphabet (letters remaining)
def remove_guess_from_alphabet():
    for i in range(len(alphabet)):
        if alphabet[i] == guess:
            alphabet[i] = "_"
            guessed.append(guess)

# Get input for if the user wants to restart the game
def play_again():
    while True:
        again = input("> ").upper()
        if again == 'Y' or again == 'YES':
            restart = True
            break
        elif again == 'N' or again == 'NO':
            restart = False
            break
        else:
            print("Invalid input.")
    return restart

print("WELCOME TO MY SHITTY HANGMAN GAME")

game_active = True

# Start the main loop
while game_active:
    playing, alphabet, guessed, max_guesses = initialize_settings()

    print("\nChoose a difficulty: EASY | MEDIUM | HARD")
    difficulty = choose_difficulty()
    print(f"You have chosen {difficulty} difficulty.")

    wordlist = generate_wordlist()
    secret_word, secret_word_string, secret_word_length, secret_word_progress = set_secret_word()
    print(f"\nThe {secret_word_length}-letter word has been chosen.")

    # Start the gameplay loop
    while playing:
        show_status()

        print("\nType a letter, or type 'ATTEMPT' to attempt to guess the full word, and press Enter.")
        guess = get_guess()
        
        if guess == 'ATTEMPT':
            print("Type out the full word and press Enter.")
            if attempt_full_word():
                secret_word_progress = secret_word
            else:
                max_guesses = 0
        else:
            instances = check_letter_instances()
            remove_guess_from_alphabet()

            if instances < 1:
                max_guesses -= 1
                print(f"\nSorry, the letter {guess} is not in the secret word.\n")
            elif instances == 1:
                print(f"\nThere is one {guess}.\n")
            else:
                print(f"\nThere are {instances} {guess}'s!\n")

        if max_guesses == 0:
            print(f"\nYou're dead... R.I.P. The secret word was {secret_word_string}.\n")
            playing = False
        elif secret_word_progress == secret_word:
            print(f"\nCongratulations, you survived! The secret word was {secret_word_string}.\n")
            playing = False

    print("Would you like to play again? YES | NO")
    if play_again():
        pass
    else:
        game_active = False
        print("\nThanks for playing!")