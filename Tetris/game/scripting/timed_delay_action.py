import time
from game.scripting.action import Action


class TimedDelayAction(Action):

    def __init__(self, delay):
        self._delay = delay
        self._start = time.time()
        
    def execute(self, cast, script, callback):
        time.sleep(self._delay)