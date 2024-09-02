class Question:
    def __init__(self,q_text,q_answer):
        self.text = q_text
        self.answer = q_answer

new_q = Question("과학 주제의 질문입니다!! 맞춰보라냥!!! ","Doo-dum boo-boom \n")
print(new_q.text,new_q.answer)