from pysics.maths import Matrix
from pysics.maths.constants import matrix_project


class Point(Matrix):
    
    """
    Class Point
    """
    
    def __new__(cls, pos):
        """
        @param vec: The (x, y, z) array of the point.
        """
        if isinstance(pos, Matrix):
            return super(Point, cls).__new__(cls, [[pos[0][0]], [pos[1][0]], [pos[2][0]], [1]])
        else:
            return super(Point, cls).__new__(cls, [[pos[0]], [pos[1]], [pos[2]], [1]])
    
    def __init__(self, pos):
        """
        @param vec: The (x, y, z) array of the point.
        """
        super(Point, self).__init__([[pos[0]], [pos[1]], [pos[2]], [1]])
        self.x, self.y, self.z = self[0][0], self[1][0], self[2][0]
    
    def project(self, cam):
        """
        Project the point to the camera.
        @param cam: The camera.
        """
        return matrix_project(cam) * self
    