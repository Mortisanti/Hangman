# Hangman
I decided to use my current Python knowledge to create a command line version of Hangman to the best of my ability.
## Difficulty Settings
As you will see, the available difficulty settings are "EASY", "MEDIUM", and "HARD". Not much thought went into the difficulties:
* EASY
    * Words with a length between 3 and 6
* MEDIUM
    * Words with a length between 7 and 10
* HARD
    * Words with a length of 11 or more
# secret_words.py
This script was originally meant to just contain a Python list of all possible words, which I was going to import into the main script. With further thought, it became the script used to shuffle the list of words and write them all to the difficulty files based on their respective lengths.