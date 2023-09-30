from pysics.rasterize import Object2D


class Point2D(Object2D):
    
    """
    2D Points
    """
    
    def __init__(self, pos):
        """
        @param pos: The position of the point.
        """
        self.pos = self.x, self.y, self.z = pos.x, pos.y, pos.z
        self.scr_pos = self.x, self.y

    def to_screen(self, scr):
        """
        Transform the point to the screen.
        @param scr: The screen.
        """
        return scr.get_width() / 2 + self.x, scr.get_height() / 2 - self.y
    