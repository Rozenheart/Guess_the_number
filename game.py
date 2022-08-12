import numpy as np

number = np.random.randint(1, 101)

count = 0

while True:
    count += 1
    predict_nums = int(input('Enter number:')) 
    if predict_nums < number:
        print(f'\nTrying number {count}\nNeed more\n')
    elif predict_nums > number:
        print(f'\nTrying number {count}\nNeed less\n')
    elif predict_nums == number:
        print(f'great! thats {predict_nums}, you needed {count} tryes')
        break