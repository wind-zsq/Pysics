from pysics.render import Object3D
from pysics.rasterize import Point2D
from pysics.maths import Point
from pysics.maths.constants import matrix_coordinate


class Point3D(Object3D):
    
    """
    3D Points
    """
    
    def __init__(self, world, pos, coordinate=None):
        """
        @param world: The world the point belongs to.
        @param pos: The relative position of the point in the coordinate.
        @param coordinate: The coordinate the point is in.
        """
        super().__init__(world)
        self.coordinate = coordinate
        self.pos = Point(pos)
    
    def to_camera(self, cam):
        """
        The relative position to the camera.
        @param cam: The camera.
        """
        return Point3D(self.world, matrix_coordinate(self.coordinate, cam) * self.pos)
    
    def project(self, cam):
        """
        Project the point to the camera.
        @param cam: The camera.
        """
        return Point2D(self.to_camera(cam).pos.project(cam))
    