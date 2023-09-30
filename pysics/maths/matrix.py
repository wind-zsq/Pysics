from numpy import matrix, array, convolve
from numpy.linalg import inv, det


class Matrix(tuple):
    """
    Class Matrix
    """

    def __new__(cls, arr):
        """
        @param arr: Contents of the matrix.
        """
        arr = tuple(map(tuple, array(arr)))
        shape = len(arr), len(arr[0])
        if cls == Matrix:
            if shape == (4, 1):
                from pysics.maths import Vector, Point
                x, y, z, w = arr[0][0], arr[1][0], arr[2][0], arr[3][0]
                if w == 0:
                    return Vector((x, y, z))
                else:
                    return Point((x / w, y / w, z / w))
            elif shape == (1, 1):
                return array[0][0]
        return super(Matrix, cls).__new__(cls, arr)

    def __init__(self, arr):
        """
        @param arr: Contents of the matrix.
        """
        self.shape = len(arr), len(arr[0])
        self.mat = matrix(self)

    def add(self, mat):
        """
        Matrix addition.
        @param mat: A matrix.
        """
        return Matrix(self.mat + mat.mat)

    def sub(self, mat):
        """
        Matrix subtraction.
        @param mat: A matrix.
        """
        return Matrix(self.mat - mat.mat)

    def mul_num(self, num):
        """
        Matrix number multiplication.
        @param num: A number.
        """
        return Matrix(self.mat * num)

    def mul_mat(self, mat):
        """
        Matrix multiplication.
        @param mat: A matrix.
        """
        return Matrix(self.mat * mat.mat)

    def transpose(self):
        """
        The transpose matrix of the matrix.
        """
        return Matrix(self.mat.transpose())

    def inverse(self):
        """
        The inverse matrix of the matrix.
        """
        if self.det != 0:
            return Matrix(inv(self.mat))
        else:
            return None

    def convolve(self, kernel):
        """
        Convolution with the kernel.
        @param kernel: The convolutional kernel.
        """
        return Matrix(convolve(kernel.mat, self.mat, "same"))

    @property
    def det(self):
        """
        The determinant of the matrix.
        """
        return det(self.mat)

    def __add__(self, other):
        """
        Matrix addition.
        """
        return self.add(other)

    def __sub__(self, other):
        """
        Matrix subtraction.
        """
        return self.sub(other)

    def __mul__(self, other):
        """
        Matrix multiplication.
        """
        if isinstance(other, int) or isinstance(other, float):
            return self.mul_num(other)
        elif isinstance(other, Matrix):
            return self.mul_mat(other)

    def __rmul__(self, other):
        """
        Matrix multiplication.
        """
        if isinstance(other, int) or isinstance(other, float):
            return self.mul_num(other)

