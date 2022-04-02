from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        body = racket.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()

        # Prevents racket from bouncing off the edge
        if x == FIELD_LEFT and velocity.get_x() < 0:
            velocity = Point(0, velocity.get_y())
        elif x == FIELD_RIGHT - RACKET_WIDTH and velocity.get_x() > 0:
            velocity = Point(0, velocity.get_y())
        
        position = position.add(velocity.scale(GRID_CELL_SIZE))

        if x < FIELD_LEFT:
            position = Point(FIELD_LEFT, position.get_y())
        elif x > (FIELD_RIGHT - RACKET_WIDTH):
            position = Point(FIELD_RIGHT - RACKET_WIDTH, position.get_y())
            
        body.set_position(position)
        return