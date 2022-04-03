from game.casting.actor import Actor


class Piece(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, image, format, debug = False):
        """Constructs a new figure of Bricks.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            format: A matrix of integars.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._format = format

    def get_body(self):
        """Gets the brick's body.
        
        Returns:
            An instance of Body.
        """
        return self._body
    
    def get_image(self):
        """Gets the brick's image.
        
        Returns:
            An instance of Image.
        """
        return self._image