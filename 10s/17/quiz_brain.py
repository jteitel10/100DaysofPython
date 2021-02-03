class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

# sets current question and gets user answer
    def next_question(self):
        curr_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curr_question.text} (True/False)\n").lower()
        self.check_answer(user_answer, curr_question.answer)


# checking to see if there is a question following
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
# check the answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print(f"Correct.\nThe correct answer was {correct_answer}.\nYour score is: {self.score}/{self.question_number}\n")
        else:
            print(f"Wrong, correct answer was {correct_answer}.\nYour score is: {self.score}/{self.question_number}\n")
