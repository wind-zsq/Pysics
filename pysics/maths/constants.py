from pysics.maths import Matrix
from math import sin, cos


world_origin = (0, 0, 0)
x_axis = (1, 0, 0)
y_axis = (0, 1, 0)
z_axis = (0, 0, 1)

matrix_identity = Matrix(
    [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]
)


def matrix_cross(vec):
    """
    The matrix used to calculate cross product.
    @param vec: A vector.
    """
    return Matrix(
        [[0, -vec.z, vec.y, 0],
         [vec.z, 0, -vec.x, 0],
         [-vec.y, vec.x, 0, 0],
         [0, 0, 0, 1]]
    )


def matrix_translation(vec):
    """
    The matrix used to translate along a vector.
    @param vec: A vector.
    """
    return Matrix(
        [[1, 0, 0, vec.x],
         [0, 1, 0, vec.y],
         [0, 0, 1, vec.z],
         [0, 0, 0, 1]]
    )


def matrix_rotation(axis, angle):
    """
    The matrix used to rotate a certain angle around the axis.
    @param axis: The rotation axis.
    @param angle: The rotating angle.
    """
    return cos(angle) * matrix_identity + (1 - cos(angle)) * axis * axis.transpose() + sin(angle) * matrix_cross(axis)


def matrix_scale(scale):
    """
    The matrix used for scaling.
    @param scale: The scales for (x, y, z) directions.
    """
    return Matrix(
        [[scale[0], 0, 0, 0],
         [0, scale[1], 0, 0],
         [0, 0, scale[2], 0],
         [0, 0, 0, 1]]
    )


def matrix_project(cam):
    """
    The matrix used to project objects to the camera.
    
    Output format:
    matrix_project(cam) * Point((x, y, z)) -> Point((x', y', z'))
    (x', y') refers to the position on the screen of the camera.
    When z varies between the near pane and the far pane of the camera, z' varies from -1 to 1. 
    
    @param cam: The camera.
    """
    return Matrix(
        [[cam.height, 0, 0, 0],
         [0, cam.height, 0, 0],
         [0, 0, (cam.near + cam.far) / (cam.far - cam.near), 2 * cam.near * cam.far / (cam.far - cam.near)],
         [0, 0, -1, 0]]
    )


def matrix_coordinate(c1, c2=None):
    """
    The matrix used to transform coordinates.
    @param c1: The original coordinate.
    @param c2: The target coordinate.
    """
    if c2 is None:
        if c1 is None:
            return matrix_identity
        else:
            return Matrix(
                [[c1.x.x, c1.y.x, c1.z.x, c1.center.x],
                 [c1.x.y, c1.y.y, c1.z.y, c1.center.y],
                 [c1.x.z, c1.y.z, c1.z.z, c1.center.z],
                 [0, 0, 0, 1]]
            )
    else:
        if c1 is None:
            return matrix_coordinate(c2).inverse()
        else:
            return matrix_coordinate(None, c2) * matrix_coordinate(c1)
