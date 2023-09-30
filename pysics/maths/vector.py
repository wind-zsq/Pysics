from pysics.maths.constants import *
from math import sqrt


class Vector(Matrix):
    
    """
    Class Vector
    """
    
    def __new__(cls, vec):
        """
        @param vec: The value array of the vector.
        """
        if isinstance(vec, Matrix):
            return super(Vector, cls).__new__(cls, [[vec[0][0]], [vec[1][0]], [vec[2][0]], [0]])
        else:
            return super(Vector, cls).__new__(cls, [[vec[0]], [vec[1]], [vec[2]], [0]])
    
    def __init__(self, vec):
        """
        @param vec: The value array of the vector.
        """
        super(Vector, self).__init__([[vec[0]], [vec[1]], [vec[2]], [0]])
        self.x, self.y, self.z = self[0][0], self[1][0], self[2][0]
    
    @property
    def norm(self):
        """
        The norm(length) of the vector.
        """
        return sqrt(sum(self[i][0] for i in range(3)))
    
    def unit(self):
        """
        The unit vector in the same direction as self.
        """
        return self * self.norm
    
    def dot(self, vec):
        """
        The dot product of two vectors.
        @param vec: A vector.
        """
        return self * vec
     
    def cross(self, vec):
        """
        The cross product of two vectors.
        @param vec: A vector.
        """
        return matrix_cross(self) * vec

