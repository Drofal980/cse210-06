from constants import *
from game.scripting.action import Action


class DrawGridAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        grid = cast.get_first_actor(GRID_GROUP)
        body = grid.get_body()

        if grid.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = grid.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)