from .object3D import *
from .vec3D import *


class Point3D(Object3D):
    """
    3D点类
    """

    def __init__(self, pos, size=1, color=(0, 0, 0), show=True):
        """
        创建一个3D点
        :param pos: 点的坐标
        :param size: 点的大小
        :param color: 点的颜色
        :param show: 是否加到点集中
        """
        self.pos = pos
        self.size = size
        self.color = color
        self.show = show
        points3D.add(self)

    def move(self, direct):
        """
        将点沿向量移动
        :param direct: 一个向量，表示移动方向及距离
        :return: 移动后得到的点
        """
        self = Point3D(tuple(self[i] + direct[i] for i in range(3)), size=self.size, color=self.color, show=self.show)
        return self

    def set_color(self, color):
        """
        给点设置颜色
        :param color: 设定的颜色
        """
        self.color = color

    def __add__(self, other):
        """
        点与向量相加，得到新的点
        :param other: 另一个向量
        :return: 新的点
        """
        return Point3D(tuple(self[i] + other[i] for i in range(3)), size=self.size, color=self.color, show=self.show)

    def __sub__(self, other):
        """
        将两个3D点类相减，得到一个向量
        :param other: 另一个3D点类
        :return: 两个点之间的向量
        """
        return Vec3D(tuple(self[i] - other[i] for i in range(3)))

    def __getitem__(self, item):
        return self.pos[item]


points3D = Objects3D()
