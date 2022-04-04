from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        all_rackets = cast.get_actors(RACKET_GROUP)
        for all_racket in all_rackets:
            racket_grid_position = all_racket.get_location_on_grid()
            grid = cast.get_first_actor(GRID_GROUP)
            column = racket_grid_position.get_x()
            row = racket_grid_position.get_y()

            print(f"R:{row} C:{column}")
            board = grid.get_matrix()
            offset = all_rackets.index(all_racket)
            if self._keyboard_service.is_key_down(LEFT) and column-offset > 0:
                if board[row][column-1-offset] != 1:
                    rackets = cast.get_actors(RACKET_GROUP)
                    for racket in rackets:
                        racket.swing_left()
            elif self._keyboard_service.is_key_down(RIGHT) and column+1 < GRID_COLUMNS and board[row][column+1] != 1: 
                rackets = cast.get_actors(RACKET_GROUP)
                for racket in rackets:
                    racket.swing_right()
            elif self._keyboard_service.is_key_down(DOWN): 
                rackets = cast.get_actors(RACKET_GROUP)
                for racket in rackets:
                    racket.move_down()
            elif self._keyboard_service.is_key_down(UP):
                rackets = cast.get_actors(RACKET_GROUP)
                for racket in rackets:
                    racket.rotate()    
            else: 
                rackets = cast.get_actors(RACKET_GROUP)
                for racket in rackets:
                    racket.stop_moving()