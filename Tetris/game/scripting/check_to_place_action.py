from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.brick import Brick
from game.casting.racket import Racket
from game.scripting.reset_racket_action import ResetRacketAction


class CheckToPlaceAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        # Racket Details
        rackets = cast.get_actors(RACKET_GROUP)

        for racket in rackets:
            body = racket.get_body()
            position = body.get_position()

            # Grid Details
            grid = cast.get_first_actor(GRID_GROUP)
            grid_position = racket.get_location_on_grid()
            column = grid_position.get_x()
            row = grid_position.get_y()
            if_block_below = True if (row+1 < 24 and grid.get_grid_position_value(row+1, column) == 1) else False

            if position.get_y() >= FIELD_BOTTOM - BRICK_HEIGHT or if_block_below:
                ResetRacketAction(cast)
                
        

