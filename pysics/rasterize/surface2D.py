from pysics.rasterize import Object2D, Point2D

from pygame.color import Color


class Surface2D(Object2D):
    """
    2D Surfaces
    """

    def __init__(self, points, color=Color(0, 0, 0)):
        """
        @param points: The points of the surface.
        @param color: The color of the surface.
        """
        self.points = tuple(map(Point2D, points))
        self.color = Color(color)

    def to_screen(self, scr):
        """
        Transform the line to the screen.
        @param scr: The screen.
        """
        return tuple(p.to_screen(scr) for p in self.points)

