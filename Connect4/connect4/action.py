class Connect4Action:
    """
    a connect 4 action is simple - it only takes the value of the column to play
    """
    __col: int

    def __init__(self, col: int):
        self.__col = col

    def get_col(self):
        return self.__col
