from constants import *
from game.scripting.action import Action
from game.casting.point import Point


class MoveBrickAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        grid = cast.get_first_actor(GRID_GROUP)
        board = grid.get_matrix()

        # board[5][1] = 1

        # for r in range(GRID_ROWS):
        #     for c in range(GRID_COLUMNS):
        #         if board[r][c] != 0 and (r+1) != GRID_ROWS:
        #             board[r+1][c] = 1
        #             board[r][c] = 0

