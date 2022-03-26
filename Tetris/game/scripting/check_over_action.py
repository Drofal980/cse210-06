from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        #Todo: Use this to check if row is complete or something
        pass
        # bricks = cast.get_actors(BRICK_GROUP)
        # Checking if no bricks are left
        # if len(bricks) == 0:
        #     stats = cast.get_first_actor(STATS_GROUP)
        #     stats.next_level()
        #     callback.on_next(NEXT_LEVEL)