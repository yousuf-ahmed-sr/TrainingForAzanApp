import random
while True:
    class Random_Question_Generator:
        def __init__(self, minimum, maximum):
            self.minimum = minimum
            self.maximum = maximum
            self.num1 = random.randint(self.minimum, maximum)
            self.num2 = random.randint(self.minimum, maximum)
            self.input_operator = random.choice(['+', '-', '*', '/'])
            self.input_question = f"{self.num1} {self.input_operator} {self.num2}"

        def create_output_question(self):
            if self.input_operator == '*':
                output_operator = 'x'
                num1, _, num2 = self.input_question.split()
                self.output_question = f"{num1} {output_operator} {num2}"
            else:
                output_operator = self.input_operator
                num1, _, num2 = self.input_question.split()
                self.output_question = f"{num1} {output_operator} {num2}"

    class get_answer:
        def __init__(self, num1, num2, operator):
            self.num1 = num1
            self.num2 = num2
            self.operator = operator
            self.answer = self.calculate_answer()

        def calculate_answer(self):
            if self.operator == '+':
                return self.num1 + self.num2
            elif self.operator == '-':
                return self.num1 - self.num2
            elif self.operator == '*':
                return self.num1 * self.num2
            elif self.operator == '/':
                return self.num1 / self.num2   # For decimal division

    try:
        maximum2 = input('Choose a difficulty and only use numbers, not "hard", "normal", or "easy":')
        maximum2 = int(maximum2)
    except ValueError:
        print(f'{maximum2} is invalid. Please use numbers, not "hard", "normal", or "easy".')
    else:
        question_generator = Random_Question_Generator(1, maximum2)
        question_generator.create_output_question()
        operator = random.choice(['+', '-', '*', '/'])  # Random operator for the answer
        answer_calculator = get_answer(num1=question_generator.num1, num2=question_generator.num2, operator=operator)
        print(question_generator.output_question)
        print(answer_calculator.answer)
