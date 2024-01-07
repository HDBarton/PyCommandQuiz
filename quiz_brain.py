class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        
    def questions_remain(self):
        return len(self.question_list) > self.question_number
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print(f"You got it right!")
            self.score += 1
        else:
            print(f"Incorrect answer")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
        
#TODO: Keep track of which questions were answered incorrectly.
#      Display these questions with their correct answers in a table format for the user at the end of the quiz.