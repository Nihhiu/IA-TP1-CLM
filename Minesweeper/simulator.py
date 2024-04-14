from Minesweeper.player import MinesweeperPlayer
from Minesweeper.state import MinesweeperState
from game_simulator import GameSimulator


class MinesweeperSimulator(GameSimulator):

    def __init__(self, player1: MinesweeperPlayer, player2: MinesweeperPlayer, num_rows: int = 6, num_cols: int = 7):
        super(MinesweeperSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the Minesweeper grid
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

    def init_game(self):
        return MinesweeperState(self.__num_rows, self.__num_cols)

    def before_end_game(self, state: MinesweeperState):
        # ignored for this simulator
        pass

    def end_game(self, state: MinesweeperState):
        # ignored for this simulator
        pass
