from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.body import Body
from game.casting.brick import Brick
from game.casting.image import Image


class UpdateBricksAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        cast.clear_actors(BRICK_GROUP)
        grid = cast.get_first_actor(GRID_GROUP)
        board = grid.get_matrix()

        for r in range(GRID_ROWS):
            for c in range(GRID_COLUMNS):
                if board[r][c] != 0:

                    x = FIELD_LEFT + c * BRICK_WIDTH
                    y = FIELD_TOP + r * BRICK_HEIGHT

                    position = Point(x, y)
                    size = Point(BRICK_WIDTH, BRICK_HEIGHT)
                    velocity = Point(0, 0)

                    body = Body(position, size, velocity)
                    image = Image(BRICK_IMAGES['b'][0])

                    brick = Brick(body, image)
                    cast.add_actor(BRICK_GROUP, brick)