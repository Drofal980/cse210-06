from artifact import Artifact

class Rock(Artifact):

    def __init__(self):
        super().__init__()
        self.__points = -1
        super().set_text("O")

    def get_points(self):
        return self.__points