"""Game: guess the number
Only PC's guesses the number"""

import numpy as np

def random_predict(number: int=1) -> int:
    """Random guesses 

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Count of attempts
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if predict_number == number:
            break
    return count

def score_game(random_predict) -> int:
    """Guesses for 1000 attempts 

    Args:
        random_predict ([type]): Guess function

    Returns:
        int: Mean of attempts
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size = 1000)
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    
    print(f'\nAlghorythm guesses average: {score}\n')
    return 'Game over'

if __name__ == '__main__':
    score_game(random_predict)
