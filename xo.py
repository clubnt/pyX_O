
class Player:

    def __init__(self, name, symbol):

        self.name = name
        self.symbol = symbol


class Game:

    MAX_STEPS = 9
    DEFAULT_SYMBOL = "_"

    def __init__(self):

        self.player_1 = Player("Игрок 1", "X")
        self.player_2 = Player("Игрок 2", "O")

        self.current_step = 0

        self.current_player = None
        self.cells = None

        self.finish_results = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def start(self):

        print("\n")
        print("_________________________________НОВАЯ_ИГРА_________________________________________")
        print("\n")

        self.cells = []
        self.current_player = self.player_1

        for i in range(3):
            self.cells.append([])
            for j in range(3):
                self.cells[i].append(self.DEFAULT_SYMBOL)

        # Game loop
        for i in range(self.MAX_STEPS):

            self.show_game_state()

            is_input_correct = False

            while not is_input_correct:
                print(self.current_player.name, "(" + self.current_player.symbol + "),", "введите номер строки и столбца: ")

                try:
                    data = input()
                except KeyboardInterrupt:
                    print("Данные не получены. Игра окончена")
                    exit(0)

                is_input_correct = self.check_input_data_correct(data)

                if not is_input_correct:
                    print("Неправильный ввод!")
                    self.show_game_state()

            column = int(data[0])
            row = int(data[1])

            self.cells[column][row] = self.current_player.symbol

            if self.check_game_finish():
                self.show_game_result("Игра закончена. Победил игрок: " + self.current_player.name)
                self.start()
            else:
                self.change_player()

        self.show_game_result("Игра закончена. Ничья!")

        self.start()

    def check_input_data_correct(self, data):

        if len(data) != 2:
            return False
        try:
            column = int(data[0])
            row = int(data[1])
        except ValueError:
            return False

        if column > 2 or row > 2 or column < 0 or row < 0:
            return False

        if self.cells[column][row] != self.DEFAULT_SYMBOL:
            return False

        return True

    def change_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def show_game_state(self):
        for i in range(len(self.cells)):
            print("| ", end="")
            for j in range(len(self.cells[i])):
                symbol = self.cells[i][j]
                print(symbol, end=" | ")
            print("\n")

    def show_game_result(self, message):

        self.show_game_state()

        print("========================================================================")
        print("************************************************************************")
        print(message)
        print("************************************************************************")
        print("========================================================================\n")

    def check_game_finish(self):

        symbol = self.current_player.symbol

        cells_inline = []

        for cols in self.cells:
            for cell in cols:
                cells_inline.append(cell)

        for result in self.finish_results:
            if cells_inline[result[0]] == symbol and cells_inline[result[1]] == symbol and cells_inline[result[2]] == symbol:
                return True
        return False


if __name__ == '__main__':
    game = Game()
    game.start()
