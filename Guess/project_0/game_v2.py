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
        if 1 <= number <= 10:
            predict_number = np.random.randint(1, 11)
            if predict_number == number:
                break
        elif 11 <= number <= 20:
            predict_number = np.random.randint(11, 21)
            if predict_number == number:
                break     
        elif 21 <= number <= 30:
            predict_number = np.random.randint(21, 31)
            if predict_number == number:
                break     
        elif 31 <= number <= 40:
            predict_number = np.random.randint(31, 41)
            if predict_number == number:
                break
        elif 41 <= number <= 50:
            predict_number = np.random.randint(41, 51)
            if predict_number == number:
                break
        elif 51 <= number <= 60:
            predict_number = np.random.randint(51, 61)
            if predict_number == number:
                break
        elif 61 <= number <= 70:
            predict_number = np.random.randint(61, 71)
            if predict_number == number:
                break
        elif 71 <= number <= 80:
            predict_number = np.random.randint(71, 81)
            if predict_number == number:
                break
        elif 81 <= number <= 90:
            predict_number = np.random.randint(81, 91)
            if predict_number == number:
                break
        elif 91 <= number <= 100:
            predict_number = np.random.randint(91, 101)
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

