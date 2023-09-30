from pysics.maths import Coordinate
from pysics.maths.constants import *

from math import pi


class Camera(Coordinate):
    
    """
    Class Camera
    """
    
    def __init__(self, world, screen, /, fov=pi/3, near=0.5, far=100):
        """
        @param world: The world the camera belongs to.
        @param screen: The display screen of the camera.
        @param fov: The angle field of view (y direction) of the camera.
        @param near: The distance from the center to the near sight pane.
        @param far: The distance from the center to the far sight pane.
        """
        Coordinate.__init__(self, world_origin, x_axis, y_axis)
        self.world = world
        self.screen = screen
        self.width, self.height = self.screen.get_width(), self.screen.get_height()
        self.fov = fov
        self.near = near
        self.far = far
    