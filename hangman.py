word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from word_list and assign it to a variable called chosen_word. Then print it.

import random
chosen_word = random.choice(word_list)
print(chosen_word)

#create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
word_length = len (chosen_word)

for position in range (word_length):
    placeholder += "_"
print(placeholder)
    
# display = []
# for placeholder in chosen_word:
#     display.append("_")
# print(display)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()
#print(guess)


#TODO-3 - Check if the letter user guessed (guess) is one of the letters in the chosen_word. print "Right" if it is, "Wrong" if it's not.
display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print (display)
            
