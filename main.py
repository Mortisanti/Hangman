#TODO Incorporate Tkinkter GUI
#TODO Create web app version using Flask?
#TODO Add ability for user to guess full word
#TODO Add support for compound words and words with spaces
#TODO Add score counter (and loss counter?)
#TODO Hints?

import random

def initialize_settings():
    playing = True
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    guessed = []
    max_guesses = 5
    return playing, alphabet, guessed, max_guesses

def choose_difficulty():
    while True:
        difficulty_chosen = input("> ").upper()
        if difficulty_chosen == "EASY" or difficulty_chosen == "MEDIUM" or difficulty_chosen == "HARD":
            break
        else:
            print("Invalid input. Try again.")
    return difficulty_chosen

def generate_wordlist():
    with open(f'{difficulty}.txt', 'r') as f:
        words = f.read()
        wordlist = words.splitlines()
    return wordlist

def set_secret_word():
    word_selection = random.randint(1, len(wordlist))
    secret_word = list(wordlist[word_selection].upper())
    secret_word_progress = ["_"] * len(secret_word)
    return secret_word, secret_word_progress

def show_status():
    print("Current progress: " + " ".join(secret_word_progress))
    print("Letters Remaining: " + " ".join(alphabet))
    print(f"Guesses Remaining: {max_guesses}")

def get_guess():
    while True:
        guess = input("Your guess: ").upper()
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
    return guess

def check_letter_instances():
    instances = 0
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            instances += 1
            secret_word_progress[i] = secret_word[i]
    return instances
        
def remove_guess_from_alphabet():
    for i in range(len(alphabet)):
        if alphabet[i] == guess:
            alphabet[i] = "_"
            guessed.append(guess)

def play_again():
    while True:
        again = input("> ").upper()
        if again == "Y" or again == "YES":
            restart = True
            break
        elif again == "N" or again == "NO":
            restart = False
            break
        else:
            print("Invalid input.")
    return restart

print("WELCOME TO MY SHITTY HANGMAN GAME")

game_active = True

while game_active:
    playing, alphabet, guessed, max_guesses = initialize_settings()

    print("\nChoose a difficulty: EASY | MEDIUM | HARD")
    difficulty = choose_difficulty()
    print(f"You have chosen {difficulty} difficulty.")

    wordlist = generate_wordlist()
    secret_word, secret_word_progress = set_secret_word()
    print("\nThe " + str(len(secret_word)) + "-letter word has been chosen.")

    while playing:
        show_status()

        print("\nType a letter and press Enter.")
        guess = get_guess()

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
            print("You've run out of guesses... R.I.P.\n")
            print("The secret word was " + "".join(secret_word) + ".\n")
            playing = False
        elif secret_word_progress == secret_word:
            print(f"Congratulations, you survived! The secret word is " + "".join(secret_word) + ".\n")
            playing = False

    print("\nWould you like to play again? YES | NO")
    if play_again():
        pass
    else:
        game_active = False
        print("\nThanks for playing!")