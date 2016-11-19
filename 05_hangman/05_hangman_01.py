#!/usr/bin/env python3

# define a function for generating a random word
def choose_word():
    return('abc')

def disp_word(word,guessed_letters):
    hidden_word=list(word)
    print(' '.join(hidden_word))
    for i in range(len(hidden_word)):
        if guessed_letters[hidden_word[i]]==0:
            hidden_word[i]='_'
    print(' '.join(hidden_word))

def word_complete(word,guessed_letters):
    cntr=0
    for i in range(len(word)):
        if guessed_letters[word[i]] == 0:
            cntr+=1
    return cntr


word = choose_word()

# main loop
num_of_trials=3
trial_no=1
guessed_letters_dict=dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)
game_end=0

while (trial_no<num_of_trials) and (game_end==0):
    # print out current state of the game
    # for example - We're guessing the word: _ _ _ _ _ _ _ _ _ _
    print('-Kolo '+str(trial_no)+' z '+str(num_of_trials)+'-')

    # for example - We're guessing the word: _ _ _ _ _ _ _ _ _ _
    disp_word(word,guessed_letters_dict)


    # let's get a letter from the user
    letter = input("Guess the letter: ")

    # make sure the letter is only one character
    # TODO

    # print the letter to see if everything is ok by now
    print("You guessed", letter)


    # determine if the letter is in the word
    if letter in word:
        guessed_letters_dict[letter]=1

    if word_complete(word,guessed_letters_dict)>0:
        game_end=1




print('konec')