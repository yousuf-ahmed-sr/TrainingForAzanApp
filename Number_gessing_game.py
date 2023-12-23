import random
secret_number=random.randint(1,100)
user_action=input("Guess a number from 1 to 100, the game will tell you if your number is greater then the secret number or smaller:")
try:
    user_action=int(user_action)
except ValueError:
    print(user_action,'is not a number')
else:
    if not user_action > 100 or user_action < 1:
        if user_action > secret_number:
            print(f"your guess {user_action} is greater than the number")
        if user_action < secret_number:
            print(f"your guess {user_action} is smaller than the number")
        if user_action == secret_number:
            print(f"your guess {user_action} is correct")
            answer=True
    else:
        print(f'{user_action} bigger than 100 or smaller than 1')