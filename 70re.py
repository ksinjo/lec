# 행맨 게임만들기 1단계 
# 단어 리스트 생성 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import random
words = ["eraser","celery","pasta","kika"]
lives = 6


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

# 키 포인트 while 반복문을 문자열을 맞추번 후 다음문자열을 맞추볼 수 있도록
# 하는 것이다

end_of_game = False

while not end_of_game:
    guess = input(" Guess a letter : ").lower()
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter
            

  #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."            
if guess not in chosen_word:
    lives -= 1
    print(f"lives:{lives}")
    if lives == 0:
        end_of_game == True
        print("Y lose")

    print(f"{' '.join(display)}")    

    if "_" not in display:
        end_of_game = True
        print("win")

