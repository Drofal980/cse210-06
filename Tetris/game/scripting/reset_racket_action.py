from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.brick import Brick
from game.casting.racket import Racket


class ResetRacketAction(Action):

    def __init__(self, cast):
        # Racket Details
        rackets = cast.get_actors(RACKET_GROUP)
        grid = cast.get_first_actor(GRID_GROUP)

        for racket in rackets:
            body = racket.get_body()
            position = body.get_position()
            offset = rackets.index(racket)
            grid_position = racket.get_location_on_grid()
            column = grid_position.get_x()
            row = grid_position.get_y()


            # Sets value in board where Racket is
            grid.set_grid_position(row, column, 1)
            #TODO: Change current piece
            # Reset position
            body.set_position(Point(position.get_x(), -GRID_CELL_SIZE))