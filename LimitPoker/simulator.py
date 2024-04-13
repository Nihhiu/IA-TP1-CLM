from LimitPoker.player import LimitPokerPlayer
from LimitPoker.state import LimitPokerState
from game_simulator import GameSimulator


class LimitPokerSimulator(GameSimulator):

    def __init__(self, player1: LimitPokerPlayer, player2: LimitPokerPlayer, num_players: int = 2):
        super(LimitPokerSimulator, self).__init__([player1, player2])
        """
        number of players
        """
        self.__num_players = num_players
        

    def init_game(self):
        return LimitPokerState(self.__num_players)

    def before_end_game(self, state: LimitPokerState):
        # ignored for this simulator
        pass

    def end_game(self, state: LimitPokerState):
        # ignored for this simulator
        pass
