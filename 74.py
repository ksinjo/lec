
import random
words = ["eraser","celery","pasta","kika","saw","kinesiology"]

chosen_word = random.choice(words)
word_count = len(chosen_word)
print(chosen_word)

word_len = len(chosen_word)
display = []
for s in range(word_len):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input(" expected spelling\n").lower()

    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("win")

