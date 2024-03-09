from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for i in range(0,len(question_data)):
    this=Question(question_data[i]["text"],question_data[i]["answer"])
    question_bank.append(this)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    print(quiz.still_has_question())

if not quiz.still_has_question():
    print("you have completed the quiz")
    print(f"your score was : {quiz.score}")


