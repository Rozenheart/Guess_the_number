"""Game: guess the number
Only PC's guesses the number"""

import numpy as np

def random_predict(number: int=np.random.randint(1, 101)) -> int:
    """Random guesses 

    Args:
        number (int, optional): Guessed number. Average 1 to 100.

    Returns:
        int: Count of attempts
    """
    list_of_range = list(range(number))
    maxum = max(list_of_range)
    minum = min(list_of_range)
    predict_number = np.random.randint(1, 101)
    count = 0
    
    while True:
        count += 1
        if predict_number < number:
            minum = predict_number
            predict_number = round((minum+maxum)/2)+1
        elif predict_number > number:
            maxum = predict_number
            predict_number = round((minum+maxum)/2)
        else:
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



