# 행맨 게임만들기 1단계 
# 단어 리스트 생성 
import random
words = ["Eraser","celery","pasta","kika"]

# 랜덤으로 단어 선택
chosen_word = random.choice(words)
word_count = len(chosen_word)
print(chosen_word)
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

# Replace with frequent function variables 
word_len = len(chosen_word)
display = []
for s in range(word_len):
    display += "_"
print(display)


guess = input(" expected spelling\n").lower()
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

for pos in range(len(chosen_word)):
    letter = chosen_word[pos]
    if letter == guess:
        display[pos] = letter
      
    
print(display)



