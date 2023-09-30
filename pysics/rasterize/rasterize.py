from pysics.rasterize import Surface2D
from pysics.maths import Matrix, Point

from math import floor, ceil
from pygame.color import Color


def in_triangle(pos, points):
    vertex = tuple(Point((p.x, p.y, 0)) for p in points)
    point = Point((pos[0], pos[1], 0))
    vector_edges = (
        vertex[1] - vertex[0],
        vertex[2] - vertex[1],
        vertex[0] - vertex[2]
    )
    vector_point = (
        point - vertex[0],
        point - vertex[1],
        point - vertex[2]
    )
    for i in range(3):
        if vector_edges[i].cross(vector_point[i]).z < 0:
            return False
    return True


def rasterize(cam):
    """
    Rasterize the objects.
    """
    pixels = Matrix([[Color(0, 0, 0) for _ in range(cam.width)] for _ in range(cam.height)])

    for s in cam.world.objects:
        left = floor(min([p.pos[0] for p in s.points]))
        right = ceil(max([p.pos[0] for p in s.points]))
        top = floor(min([p.pos[1] for p in s.points]))
        bottom = ceil(max([p.pos[1] for p in s.points]))
        for x in range(left, right + 1):
            for y in range(top, bottom + 1):
                pos = x + 0.5, y + 0.5
                if in_triangle(pos, s.points):
                    # TODO Rasterize, Z-Buffer
                    pixels[x][y] += s.color
