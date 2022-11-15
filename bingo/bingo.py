from random import randint


def lines_win(cardboard):
    lines = []
    for row in cardboard:
        if row.count("*") == 5:
            lines.append(True)
        else:
            lines.append(False)
    return lines


class Bingo:
    def __init__(self, n_cardboards):
        self.cardboards = self.__get_cardboards(10)
        self.player_cardboards = self.cardboards[:n_cardboards]
        self.cpu_cardboards = self.cardboards[:10 - n_cardboards]
        self.player_points = 0
        self.cpu_points = 0

    # ------------------------------- Debug methods ------------------------------ #
    def print_status(self):
        print("Cartones jugador:", len(self.player_cardboards))
        print("Puntos jugador:", self.player_points)
        print("Cartones cpu:", len(self.cpu_cardboards))
        print("Puntos cpu:", self.cpu_points)

    # ------------------------------ Public methods ------------------------------ #
    def start_game(self):
        print("¡¡¡ Bienvenido al Fiubingo(? !!!")
        while 1:
            self.__input_handler()

    # ------------------------------ Private Methods ----------------------------- #

    def __input_handler(self):
        user_input = input(
            "Tirar bolillero [T] [t] / Cantar linea [L] [l] / Cantar bingo [B] [b]\n"
        ).capitalize()

        action_lut = {
            "T": "Tirando bolillero...",
            "L": "Linea!!",
            "B": "Bingo!!"
        }

        action = action_lut.get(user_input)
        if action:
            print(action)
        else:
            print(
                "Ocurrio un error :( -> Ingresaste una letra incorrecta. Volve a intentarlo!!"
            )

    def __select_no_duplicates(self, pool, rows, n):
        selection = []
        for i in range(rows):
            row = [col.pop(randint(0, len(col)-1)) for col in pool]
            for j in range(n//rows - 1):
                index = randint(0, len(row)-1)
                while row[index] == "X":
                    index = randint(0, len(row)-1)
                row[index] = "X"
            selection.append(row)
        return selection

    def __get_carboard(self):
        pool = list(list(range(1 + 11 * i, 12 + 11 * i)) for i in range(9))
        return self.__select_no_duplicates(pool, 3, 15)

    def __get_cardboards(self, n):
        cardboards = []
        while len(cardboards) < n:
            cardboard = self.__get_carboard()
            if cardboard not in cardboards:
                cardboards.append(cardboard)
        return cardboards


game_1 = Bingo(5)

game_1.print_status()
game_1.start_game()
