from random import randint

from Minesweeper.action import MinesweeperAction
from Minesweeper.player import MinesweeperPlayer
from Minesweeper.state import MinesweeperState
from state import State


class MinesweeperRandomBot(MinesweeperPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: MinesweeperState):
        return MinesweeperAction(randint(0, state.get_num_cols()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
