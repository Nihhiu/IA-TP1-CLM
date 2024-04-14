from random import randint

from Connect4.action import Connect4Action
from Connect4.player import Connect4Player
from Connect4.state import Connect4State
from state import State


class Connect4RandomBot(Connect4Player):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: Connect4State):
        return Connect4Action(randint(0, state.get_num_cols()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
