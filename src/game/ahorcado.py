from figure import ahorcado_figure, ahorcado_game_over, ahorcado_you_win, ahorcado_welcome

class Ahorcado:

    def __init__(self, palabra):
        self.palabra = palabra
        self.palabra_oculta = ["_"] * len(palabra)
        self.intentos = 0
        self.letras_usadas = []
        self.letras_correctas = []
        self.letras_incorrectas = []
        self.gano = False
        self.perdio = False

    def start_game(self):
        print(ahorcado_welcome)
        player_name = input("Ingresa tu nombre: ")
        print("Hola {}!".format(player_name))
        print("La palabra tiene {} letras".format(len(self.palabra)))
        print("{}".format(" ".join(self.palabra_oculta)))
        self.steps_game()

    def steps_game(self):
        while not self.gano and not self.perdio:
            letra = input('Ingresa la letra:')
            if len(letra) > 1:
                print('** Debes ingresar solo UNA letra **')
                continue
            if not letra.isalpha():
                print('**CARACTER NO VALIDO **')
                continue
            self.guess_word(letra)
            if len(ahorcado_figure) == self.intentos+1:
                self.perdio = True
                print(ahorcado_game_over)
                print(f'**LA PALABRA ERA: {self.palabra}**')

    def guess_word(self, letra):
        letra = letra.lower()
        if letra in self.palabra:
            self.letras_correctas.append(letra)
            self.letras_usadas.append(letra)
            self.update_hide_word(letra)
        else:
            self.letras_incorrectas.append(letra)
            self.letras_usadas.append(letra)
            self.intentos += 1

        print(ahorcado_figure[self.intentos])
        print("Letras incorrectas: {}".format(self.letras_incorrectas))
        print("Letras usadas: {}".format(self.letras_usadas))
        print("{}".format(" ".join(self.palabra_oculta)))

    def update_hide_word(self, letra):
        for i in range(len(self.palabra)):
            if letra == self.palabra[i]:
                self.palabra_oculta[i] = letra
        if "_" not in self.palabra_oculta:
            print(ahorcado_you_win)
            self.gano = True
            return True
        return False