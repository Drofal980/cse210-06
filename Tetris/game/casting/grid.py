from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Grid(Actor):
    """A grid background."""
    
    def __init__(self, body, image, matrix, debug = False):
        """Constructs a new Grid.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._matrix = matrix

    def get_body(self):
        """Gets the grid's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the grid's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_matrix(self):
        """Gets the grid's image.
        
        Returns:
            An instance of Image.
        """
        return self._matrix
    
    def set_matrix(self, matrix):
        """Sets the grid's matrix to the given value.

        Args:
            matrix: A matrix containing a list of integers.
        """
        self._matrix = matrix