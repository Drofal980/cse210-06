from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        racket_grid_position = racket.get_location_on_grid()
        grid = cast.get_first_actor(GRID_GROUP)
        column = racket_grid_position.get_x()
        row = racket_grid_position.get_y()
        board = grid.get_matrix()

        if self._keyboard_service.is_key_down(LEFT) and board[row][column-1] != 1:
            racket.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT) and (column+1 < 10 and board[row][column+1] != 1): 
            racket.swing_right()
        elif self._keyboard_service.is_key_down(DOWN): 
            racket.move_down()
        elif self._keyboard_service.is_key_down(UP): 
            racket.rotate()    
        else: 
            racket.stop_moving()