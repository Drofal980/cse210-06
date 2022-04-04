from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.brick import Brick
from game.casting.racket import Racket


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        grid = cast.get_first_actor(GRID_GROUP)
        board = grid.get_matrix()

        for column in range(GRID_COLUMNS):
            if board[0][column] != 0:
                #TODO: CHANGE TO END GAME SCREEN
                pass
        
        
