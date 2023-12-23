import pickle

def CreateFunction(name, code, parameter):
    exec(f'def {name}({parameter}): {code}')
    all_code = f'def {name}({parameter}): {code}'
    with open('customfunction.py', 'w') as file:
        file.write(all_code)
    
    # Pickle the function code and save it to a file
    with open('customfunction.pickle', 'wb') as file:
        pickle.dump(all_code, file)

name = input('Function name:')
code = input('Function code:')
parameter = input('Function parameter:')

CreateFunction(name, code, parameter)
