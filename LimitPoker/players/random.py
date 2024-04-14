from random import randint

from LimitPoker.action import LimitPokerAction
from LimitPoker.player import LimitPokerPlayer
from LimitPoker.state import LimitPokerState
from state import State


class LimitPokerRandomBot(LimitPokerPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: LimitPokerState):
        return LimitPokerAction(randint(0, state.get_num_cols()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
