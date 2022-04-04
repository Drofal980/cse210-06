from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.brick import Brick
from game.casting.racket import Racket


class CheckForTetris(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        grid = cast.get_first_actor(GRID_GROUP)
        board = grid.get_matrix()
        row_counter = 0

        for row in range(GRID_ROWS):
            if all(board[row]) and board[row][0] == 1:
                # Removes row
                board.remove(board[row])
                board.insert(0, [0 for i in range(GRID_COLUMNS)])
                row_counter += 1
            
        # Adds to score
        stats = cast.get_first_actor(STATS_GROUP)
        points = int(POINTS_ROW_COMPLETE * row_counter)
        stats.add_points(points)
        #TODO: Play sound
        # if points > 1:
        row_counter = 0

        
        
