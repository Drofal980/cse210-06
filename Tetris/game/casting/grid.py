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
        """Sets the grid's matrix to the given matrix.

        Args:
            matrix: A List containing lists of integers.
        """
        self._matrix = matrix
    
    def set_grid_position(self, row, column, value = int):
        """Sets a value in the grid's matrix to the given value.

        Args:
            point: An instance of Point
            value: An integar value
        """

        board = self.get_matrix()
        board[row][column] = value
        self.set_matrix(board)
    
    def get_grid_position_value(self, row = int, column = int):
        """Returns a value in a position in the grid's matrix.

        Args:
            column: An integar describing the position in a list
            row: An integar describing the position in a list
        """
        board = self.get_matrix()
        value = board[row][column]
        print(f"row: {row}, column: {column}")
        return value
        