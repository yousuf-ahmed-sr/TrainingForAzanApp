while True:
    stop=0
    num1=input('give me one number that you want to add subtract multiply divde or use power:')
    try:
        num1=float(int(num1))
    except ValueError:
        print(f'{num1} is invalid')
        stop=1
    if not stop == 1:
        operater=input('now do you want to + add - subtract * multiply / divide or use ^ power:')
        num2=input('now put the last number here:')
        try:
            num2=float(int(num2))
        except ValueError:
            print(f'{num2} is invalid')
            stop=1
    if not stop==1:
        if operater == '+':
            _answer_=num1 + num2
        elif operater == '-':
            _answer_=num1 - num2
        elif operater == '*':
            _answer_=num1 - num2
        elif operater == '/' and not num1 ==  0:
            answer_=float(num1) / float(num2)
        if num1 ==  0 :
            if not num2 == 0 :
                print('NaN')
            else:
                print('0 is the answer')
        if operater == '^':
            _answer_=num1 ** num2
            print(f'{_answer_} is the answer')