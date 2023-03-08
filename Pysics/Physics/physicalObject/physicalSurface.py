from .physicalObject import *
from ..virtualObject import *


class PhysicalSurface(PhysicalObject):
    """
    物理物体外表面类
    """

    def __init__(self, points):
        """
        创建表面
        @param points: 3个顶点（元组），按逆时针决定法向量
        """
        self.points = tuple(RenderPoint(p) for p in points)
        self.center = RenderPoint(
            (
                (points[0][0] + points[1][0] + points[2][0]) / 3,
                (points[0][1] + points[1][1] + points[2][1]) / 3,
                (points[0][2] + points[1][2] + points[2][2]) / 3
            )
        )
        PhysicalObject.__init__(self, self.center, mass = 0)

        # Normal vector of the surface
        self.normal = ((self.points[1] - self.points[0]) **
                     (self.points[2] - self.points[0])).to_len()

        self.collide = SurfaceField()

    def move(self):
        """
        移动平面
        """
        for each in self.points:
            each.move(self.linear_velocity)

    def rotate(self, center):
        """
        绕中心旋转平面
        @param center: 旋转中心
        """
        # TODO
        pass

    def update(self):
        """
        每帧刷新
        """
        self.linear_velocity += self.linear_acceleration
        self.angular_velocity += self.angular_acceleration


