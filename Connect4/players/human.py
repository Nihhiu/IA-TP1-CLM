from Connect4.action import Connect4Action
from Connect4.player import Connect4Player
from Connect4.state import Connect4State


class Connect4HumanPlayer(Connect4Player):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: Connect4State):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                return Connect4Action(int(input(f"Player {state.get_acting_player()}, choose a column: ")))
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: Connect4State):
        # ignore
        pass

    def event_end_game(self, final_state: Connect4State):
        # ignore
        pass
