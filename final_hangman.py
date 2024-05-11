from hangman_words import word_list
from hangman_art import logo,stages
import random
# 목숨 추가 
lives = 6
x = 0

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
word_count = len(chosen_word)
print(chosen_word)

display = []
for s in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input(" expected spelling\n").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
 
    if guess not in chosen_word:
        lives -= 1
        x += 1
        print(f"Y are trying {x} times")
        if lives == 0:
            end_of_game = True
            print("You lose.")


    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("win")

    print(stages[lives])