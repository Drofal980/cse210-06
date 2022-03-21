from game.casting.actor import Actor
from game.shared.point import Point

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    """A visible, unmoveable thing that participates in the game. 
    
    The responsibility of Artifact is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """
    def __init__(self):
        self._message = ""
        self._velocity = Point(0, 0)

    def set_message(self, message):
        self._message = message

    def get_message(self):
        return self._message

    def set_text(self, text):
        return super().set_text(text)

    def get_text(self):
        return super().get_text()

    def set_font_size(self, font_size):
        return super().set_font_size(font_size)
    
    def set_color(self, color):
        return super().set_color(color)

    def set_position(self, position):
        return super().set_position(position)
    
    def set_velocity(self, velocity):
        return super().set_velocity(velocity)

    def get_velocity(self, velocity):
        return super().get_velocity(velocity)
    
    def move_next(self, max_x, max_y):
        return super().move_next(max_x, max_y)

    

    