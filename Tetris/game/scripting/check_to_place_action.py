from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.brick import Brick
from game.casting.racket import Racket


class CheckToPlaceAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        #Todo: Use this to check if row is complete or something
        racket = cast.get_first_actor(RACKET_GROUP)
        body = racket.get_body()
        position = body.get_position()
        grid = cast.get_first_actor(GRID_GROUP)
        x = position.get_x()
        y = position.get_y()
        column = int((x-FIELD_LEFT) / BRICK_WIDTH)
        row = int((y-FIELD_TOP) / BRICK_HEIGHT)

        if position.get_y() >= FIELD_BOTTOM - BRICK_HEIGHT or grid.get_grid_position_value(row+1, column) == 1:
            # Sets value in board where Racket is
            grid.set_grid_position(row, column, 1)
            #Todo: Change current piece
            body.set_position(Point(CENTER_X - BRICK_WIDTH, BRICK_WIDTH))
        
