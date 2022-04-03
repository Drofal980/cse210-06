from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.brick import Brick
from game.casting.racket import Racket


class CheckToPlaceAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        # Racket Details
        racket = cast.get_first_actor(RACKET_GROUP)
        body = racket.get_body()
        position = body.get_position()

        # Grid Details
        grid = cast.get_first_actor(GRID_GROUP)
        grid_position = racket.get_location_on_grid()
        column = grid_position.get_x()
        row = grid_position.get_y()
        if_block_below = True if (row+1 < 24 and grid.get_grid_position_value(row+1, column) == 1) else False

        if position.get_y() >= FIELD_BOTTOM - BRICK_HEIGHT or if_block_below:
            # Sets value in board where Racket is
            grid.set_grid_position(row, column, 1)
            #Todo: Change current piece
            body.set_position(Point(CENTER_X - BRICK_WIDTH, BRICK_WIDTH))
        

