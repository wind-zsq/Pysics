from pysics.maths import Vector, Point
from pysics.maths.constants import matrix_translation, matrix_rotation


class Coordinate:
    
    """
    A coordinate system which determines an object's position and direction.
    """
    
    def __init__(self, center, x_dir, y_dir):
        """
        @param center: The center position of the coordinate.
        @param x_dir: The x-axis of the coordinate.
        @param y_dir: The y-axis of the coordinate.
        """
        self.center = Point(center)
        self.x = Vector(x_dir).unit()
        self.y = Vector(y_dir).unit()
        self.z = self.x.cross(self.y).unit()
        
    def move(self, dir):
        """
        Move the coordinate.
        @param dir: A vector.
        """
        self.center = matrix_translation(Vector(dir)) * self.center
    
    def rotate(self, axis, angle):
        """
        Rotate the coordinate. 
        @param axis: The rotation axis.
        @param angle: The rotating angle.
        """
        self.x = matrix_rotation(axis, angle) * self.x
        self.y = matrix_rotation(axis, angle) * self.y
        self.z = matrix_rotation(axis, angle) * self.z
    
    