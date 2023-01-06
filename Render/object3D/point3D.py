from .object3D import *
from .vec3D import *


class Point3D(Object3D):  # 3D点类
    def __init__(self, pos, size=1, color=(0, 0, 0), add=True):
        """
        创建一个三维点
        :param pos: 点的三维坐标
        :param add: 点是否加到点集中
        """
        self.pos = pos
        self.size = size
        self.color = color
        if add:
            points3D.add(self)

    def move(self, direct):
        """
        将点沿向量移动
        :param direct: 一个向量，表示移动方向及距离
        :return: 移动后得到的点坐标
        """
        for i in range(3):
            self[i] += direct[i]

    def setColor(self, color):
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
        return Point3D(tuple([self[i] + other[i] for i in range(3)]), size=self.size, color=self.color)

    def __sub__(self, other):
        return Vec3D(tuple([self[i] - other[i] for i in range(3)]))

    def __iter__(self):
        return iter(self.pos)

    def __getitem__(self, item):
        return self.pos[item]


points3D = Objects3D()
