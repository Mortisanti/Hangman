#TODO Add guess failures, subtract guesses
#TODO Difficulty selection
#TODO English dictionary, randomly selects word
#TODO Convert this entire project to Wheel of Fortune: Metalhead Edition

secret_word = list("BUTTS")
secret_word_progress = ["_"] * len(secret_word)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
guess_list = []
number_of_guesses = 6
game_active = True

while game_active:
    print("Welcome to my shitty Hangman game!")
    print("Choose a letter and press Enter.")
    guess = input().upper()

    while len(guess) != 1 or guess not in alphabet:
        print("Invalid input. Try again")
        guess = input().upper()
    
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            secret_word_progress[i] = secret_word[i]
        
    print(" ".join(secret_word_progress))


    break