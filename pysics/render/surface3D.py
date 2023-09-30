from pysics.maths import Point
from pysics.maths.constants import matrix_coordinate
from pysics.render import Object3D
from pysics.rasterize import Surface2D

from pygame.color import Color


class Surface3D(Object3D):
    """
    3D Surfaces
    """

    def __init__(self, world, points, color=Color(0, 0, 0), /, coordinate=None):
        """
        @param world: The world the surface belongs to.
        @param points: The points of the surface.
        @param color: The color of the surface.
        @param coordinate: The coordinate the surface is in.
        """
        super().__init__(world)
        self.coordinate = coordinate
        self.color = Color(color)
        self.points = tuple(map(Point, points))
        self.normal = (self.points[0] - self.points[1]).cross(self.points[1] - self.points[2]).unit()

    def to_camera(self, cam):
        """
        The relative position to the camera.
        @param cam: The camera.
        """
        return Surface3D(
            self.world,
            tuple(matrix_coordinate(self.coordinate, cam) * p for p in self.points)
        )

    def project(self, cam):
        """
        Project the line to the camera.
        @param cam: The camera.
        """
        return Surface2D(
            tuple(p.project(cam) for p in self.to_camera(cam).points)
        )
