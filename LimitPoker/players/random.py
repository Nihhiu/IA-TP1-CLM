from random import randint

from src.games.connect4.action import Connect4Action
from src.games.connect4.player import Connect4Player
from src.games.connect4.state import Connect4State
from src.games.state import State


class RandomLimitPokerPlayer(Connect4Player):

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
