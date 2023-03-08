from ...Render import *


class Force:
    """
    力类
    """

    def __init__(self, direct, point):
        """
        创建一个力
        @param direct: 力的方向
        @param point: 力的作用点
        """
        self.direct = Vector(direct)
        self.point = RenderPoint(point)

    def __add__(self, other):
        """
        力的合成
        @param other: 另一个与其共点的力
        @return: 两个力的合力
        """
        if self.point == other.point:
            direct = self.direct + other.direct
            return Force(direct, self.point)

    def __mul__(self, other):
        return Force(self.direct.multi_len(other), self.point)