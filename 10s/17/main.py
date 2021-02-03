from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


# created a bank of question objects from the question data
question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# create quiz object
quiz = QuizBrain(question_bank)

# continue playing game if there are still questions
while quiz.still_has_questions():
    quiz.next_question()
print("You have finished the quiz.")
print(f"Your score was: {quiz.score}/{quiz.question_number}")
