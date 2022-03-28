from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Grid(Actor):
    """A grid background."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Grid.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the ball's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image