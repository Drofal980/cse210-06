from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        self.move_counter = 0
        
    def execute(self, cast, script, callback):
        #Todo: Use this to check if row is complete or something
        racket = cast.get_first_actor(RACKET_GROUP)
        if self.move_counter >= RACKET_FALL_COUNTER_MAX:
            racket.move_down()
            self.move_counter = 0
        else:
            self.move_counter += RACKET_FALL_COUNTER_MAX
