from constants import *
from game.scripting.action import Action
from game.casting.point import Point


class CheckOverAction(Action):

    def __init__(self):
        self.move_counter = 0
        
    def execute(self, cast, script, callback):
        #Todo: Use this to check if row is complete or something
        racket = cast.get_first_actor(RACKET_GROUP)
        body = racket.get_body()
        position = body.get_position()

        if position.get_y() > FIELD_BOTTOM:
            body.set_position(Point(CENTER_X - BRICK_WIDTH, BRICK_WIDTH))
            #Todo: Change current piece
            #Todo: Place brick and set value in matrix
        elif self.move_counter >= RACKET_FALL_COUNTER_MAX:
            racket.move_down()
            self.move_counter = 0
        else:
            self.move_counter += RACKET_FALL_COUNTER_RATE
        
