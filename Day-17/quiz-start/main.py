from question_model import Question
from data import question_data 
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions(): 
    quiz.next_question()

print("U've completed the quz") # 모든 퀴즈가 끝났을 때 출력
print(f"U final Score was : {quiz.score} / {quiz.question_number}") # 모든 퀴즈 종료 후 점수 출력 
# len = len(question_data)
# print(len)
# print(question_data[1]["text"])