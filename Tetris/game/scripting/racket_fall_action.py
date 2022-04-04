from constants import *
from game.scripting.action import Action
from game.casting.racket import Racket


class RacketFallAction(Action):

    def __init__(self):
        self.move_counter = 0
        
    def execute(self, cast, script, callback):
        if self.move_counter >= RACKET_FALL_COUNTER_MAX:
            rackets = cast.get_actors(RACKET_GROUP)

            for racket in rackets:
                racket.move_down()
            self.move_counter = 0
        else:
            self.move_counter += RACKET_FALL_COUNTER_RATE
        
