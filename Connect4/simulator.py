from Connect4.player import Connect4Player
from Connect4.state import Connect4State
from game_simulator import GameSimulator


class Connect4Simulator(GameSimulator):

    def __init__(self, player1: Connect4Player, player2: Connect4Player, num_rows: int = 6, num_cols: int = 7):
        super(Connect4Simulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the connect4 grid
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

    def init_game(self):
        return Connect4State(self.__num_rows, self.__num_cols)

    def before_end_game(self, state: Connect4State):
        # ignored for this simulator
        pass

    def end_game(self, state: Connect4State):
        # ignored for this simulator
        pass
