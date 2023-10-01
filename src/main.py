from sys import path
path.append('src/game/')

from get_words import get_word
from ahorcado import Ahorcado


word = get_word()
game = Ahorcado(word)
game.start_game()