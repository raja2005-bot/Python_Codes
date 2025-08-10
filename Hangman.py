import random
from hangman_words import stages
from hangman_words import word_list


lives = 6



#1. randomly choose the word from the list
word = random.choice(word_list)
print(word)



placeholder = ""
for position in range(0, len(word)):
    placeholder+="_"
print(placeholder)


game_over = False
correct_letter = []
while not game_over:
    user_guess = input("Guess a letter : ").lower()


    if user_guess in correct_letter:
        print("You have already guessed the letter!!!")
        continue


    display = ""
    for letter in word:
        if user_guess == letter:
            display += letter
            correct_letter.append(user_guess)
        elif letter in correct_letter:
            display+=letter
        else:
            display += "_"
    print(display)

    if user_guess not in word:
        lives -=1
        if lives == 0:
            print("You Lose the word was:", word)
            break


    if "_" not in display :
        game_over = True
        print("Game Over")

    print(stages[lives])





