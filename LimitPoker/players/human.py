from LimitPoker.action import LimitPokerAction
from LimitPoker.player import LimitPokerPlayer
from LimitPoker.state import LimitPokerState


class LimitPokerHumanPlayer(LimitPokerPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: LimitPokerState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                return LimitPokerAction(int(input(f"Player {state.get_acting_player()}, choose a column: ")))
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: LimitPokerState):
        # ignore
        pass

    def event_end_game(self, final_state: LimitPokerState):
        # ignore
        pass
