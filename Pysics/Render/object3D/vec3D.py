from math import *

from .object3D import *


class Vec3D(Object3D, tuple):
    """
    3D向量类
    """

    def __init__(self, direct):
        """
        以原点为起点创建一个三维向量，不能为零向量
        :param direct: 表示向量的坐标
        """
        tuple.__init__(direct)

    def to_len(self, length=1):
        """
        得到指定长度的新向量
        :param length: 指定的长度
        :return: 新向量
        """
        return Vec3D(tuple(x / self.len * length for x in self))

    @property
    def len(self):  # 模长
        """
        得到向量的模长
        :return: 向量的模长
        """
        return sqrt(sum(x ** 2 for x in self))

    def rotate(self, x, y, z):
        """
        旋转这个向量
        :param x: 绕x轴旋转度数
        :param y: 绕y轴旋转度数
        :param z: 绕z轴旋转度数
        :return: 旋转后的向量
        """
        # 绕x轴
        x, y, z = x / 180 * pi, y / 180 * pi, z / 180 * pi
        new = (self[0],
               self[1] * cos(x) - self[2] * sin(x),
               self[1] * sin(x) + self[2] * cos(x))
        # 绕y轴
        new = (self[0] * cos(y) + self[2] * sin(y),
               self[1],
               self[2] * cos(y) - self[0] * sin(y))
        # 绕z轴
        new = (self[0] * cos(z) - self[1] * sin(z),
               self[0] * sin(z) + self[1] * cos(z),
               self[2])
        return Vec3D(new)

    def pos_direct(pos):
        x, y = pos
        if x > 0:
            if y != 0:
                return (2 * pi + atan(y / x)) % (2 * pi)
            else:
                return 0
        elif x < 0:
            if y != 0:
                return pi + atan(y / x)
            else:
                return pi
        else:
            if y > 0:
                return pi / 2
            elif y < 0:
                return pi * 3 / 2
            else:
                return pi / 2

    def __len__(self):
        """
        得到向量的模长
        :return: 向量的模长
        """
        return sqrt(sum(x ** 2 for x in self))

    def __add__(self, other):  # 加法
        """
        两个向量相加
        :param other: 另一个向量（可交换）
        :return: 和向量
        """
        return Vec3D((self[i] + other[i] for i in range(3)))

    def __sub__(self, other):  # 减法
        """
        两个向量相减
        :param other: 另一个向量（不可交换）
        :return: 差向量
        """
        return Vec3D(tuple(self[i] - other[i] for i in range(3)))

    def __mul__(self, other):  # 点乘
        """
        两个向量的点积（数量积）
        :param other: 另一个向量（可交换）
        :return: 向量的点积
        """
        return sum(self[i] * other[i] for i in range(3))

    def __pow__(self, other):  # 叉乘
        """
        两个向量的叉乘（向量积）
        :param other: 另一个向量（不可交换）
        :return:
        """
        ax, ay, az = self
        bx, by, bz = other
        return Vec3D((ay * bz - az * by, az * bx - ax * bz, ax * by - ay * ax))
