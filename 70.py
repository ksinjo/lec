#행맨 글자의 무작위 단어 선택
import random
word_list = ["eighteen","eighteen","goggles"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word  = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# 사용자에 문자를 추측하고 변수에 답을 할당하도록 요청. 추측 시 소문자로 만들어라. 
# .lower() 메서드 형태로 사용해야 한다. input() 함수를 통해 받은 문자 리터럴을 .lower() 소문자 변환 
word_count = len(chosen_word)
print(f"선택된 글자의 수는 {word_count}")
guess =input("Guess a letter \n").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess: 
        print("Bingo")
    else:
        print("wrong")