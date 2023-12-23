import random

class Random_Question_Generator:
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        num1 = random.randint(self.minimum, self.maximum)
        num2 = random.randint(self.minimum, self.maximum)
        self.input_operator = random.choice(['+', '-', '*', '/'])
        self.input_question = f"{num1} {self.input_operator} {num2}"

    def create_output_question(self):
        if self.input_operator == '*':
            output_operator = 'x'
            num1, _, num2 = self.input_question.split()
            self.output_question = f"{num1} {output_operator} {num2}"
        else:
            output_operator = self.input_operator
            num1, _, num2 = self.input_question.split()
            self.output_question = f"{num1} {output_operator} {num2}"

class get_answer(Random_Question_Generator):
    def __init__(self,answer,num1,num2,operater):
        self.operater=operater
        self.num1=num1
        self.num2=num2
        if self.operater == '+':
            answer=self.num1+self.num2
        elif self.operater == '-':
            answer=self.num1-self.num2
        elif self.operater == '*':
            answer=self.num1*self.num2
        elif self.operater == '/':
            answer=self.num1/self.num2

try:
    maximum2 = input('Choose a difficulty and only use numbers, not "hard", "normal", or "easy":')
    maximum2 = int(maximum2)
except ValueError:
    print(f'{maximum2} is invalid. Please use numbers, not "hard", "normal", or "easy".')
else:
    question_generator = Random_Question_Generator(1, maximum2)
    question_generator.create_output_question()
    answer_generator = Random_Question_Generator(minimum=question_generator.minimum, maximum=question_generator.maximum)
    answer_generator.create_output_question()
    question_generator.create_output_question()
    print(question_generator.output_question)
    print(answer_generator.input_question)