
import random

def get_word():
    with open('./game/words.txt', 'r') as file:
        words_without_spaces = file.read().replace(' ', '')
        words_array = str.split(words_without_spaces, ',')
        random_number = random.randint(0, len(words_array) - 1)
        return words_array[random_number]
