from Minesweeper.action import MinesweeperAction
from Minesweeper.player import MinesweeperPlayer
from Minesweeper.state import MinesweeperState


class MinesweeperHumanPlayer(MinesweeperPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: MinesweeperState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                return MinesweeperAction(int(input(f"Player {state.get_acting_player()}, choose a column: ")))
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: MinesweeperState):
        # ignore
        pass

    def event_end_game(self, final_state: MinesweeperState):
        # ignore
        pass
