from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        #Todo: Use this to check if row is complete or something
        grid = cast.get_first_actor(GRID_GROUP)
        board = grid.get_matrix()
        
        for r in range(GRID_ROWS):
            # Checking if no bricks are left
            if all(board[r]):
                board.remove(board[r])
                board.append([0 for i in range(GRID_COLUMNS)])
                grid.set_matrix(board)
