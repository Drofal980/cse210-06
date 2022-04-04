from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.brick import Brick
from game.casting.racket import Racket


class CheckAllBlocksInRacket(Action):

    def __init__(self, cast):
        self.check(cast)
        
    def check(self, cast):
        block_count = 0
        rackets = cast.get_actors(RACKET_GROUP)
        for racket in rackets:
            racket_grid_position = racket.get_location_on_grid()
            grid = cast.get_first_actor(GRID_GROUP)
            column = racket_grid_position.get_x()
            row = racket_grid_position.get_y()
            board = grid.get_matrix()
            
            if board[row][column+1] != 1:
                return True
            elif board[row][column-1] != 1 and column-1 > 0:
                return True
            
            return False    
                