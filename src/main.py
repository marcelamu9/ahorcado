
from sys import path
path.append('game/')

from ahorcado import Ahorcado
from get_words import get_word

word = get_word()

game = Ahorcado(word)
game.start_game()