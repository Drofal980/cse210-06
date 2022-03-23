import os
import random

from game.casting.actor import Actor
from game.casting.block import Block
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 200
MAX_Y = 480
CELL_SIZE = 20
FONT_SIZE = 20
COLS = 10
ROWS = 20
CAPTION = "Tetris"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 1


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = 0
    position = Point(x, y)

    controller = Actor()
    controller.set_text("#")
    controller.set_font_size(FONT_SIZE)
    controller.set_color(WHITE)
    controller.set_position(position)

    cast.add_actor("controllers", controller)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()