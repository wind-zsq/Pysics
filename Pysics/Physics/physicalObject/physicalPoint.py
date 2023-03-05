from .physicalObject import *


class Point3D(PhysicalObject):
    """
    物理质点类
    """

    def __init__(self, mass, pos, gravity):
        """
        创建新的物理质点
        :param mass: 质点的质量
        :param pos: 质点的初始坐标
        """
        PhysicalObject.__init__(self, pos, mass, gravity)

    def move(self):
        """
        移动物体
        """
        self.center.move(self.linear_velocity)

    def rotate(self):
        """
        转动物体
        """
        # TODO
        pass

    def update(self):
        """
        每帧刷新
        """
        self.linear_velocity += self.linear_acceleration
        self.angular_velocity += self.angular_acceleration

        self.move()
