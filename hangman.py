word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from word_list and assign it to a variable called chosen_word. Then print it.

import random
chosen_word = random.choice(word_list)
print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: \n").lower()
print(guess)
#TODO-3 - Check if the letter user guessed (guess) is one of the letters in the chosen_word. print "Right" if it is, "Wrong" if it's not.

if guess in chosen_word:
    print("Right")
else:
    print("Wrong")
            
