# This is a small quiz game designed to serve as a template for a student to fill in for test prep in any given class.
# Any part of this may be written over, all values are only demonstrations of how to easily fill in the program.
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
quiz.next_question()