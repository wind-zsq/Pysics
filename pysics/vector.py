from math import sqrt, sin, cos


class Vector(tuple):
    """
    3D向量类
    """

    def __init__(self, direct):
        """
        以原点为起点创建一个三维向量，不能为零向量
        @param direct: 表示向量的坐标
        """
        tuple.__init__((direct[0], direct[1], direct[2]))

    def to_len(self, length = 1):
        """
        得到指定长度的新向量
        @param length: 指定的长度
        @return: 新向量
        """
        return Vector(tuple(x / self.len * length for x in self))

    def multi_len(self, times):
        """
        得到指定倍数的新向量
        @param times: 指定的倍数
        @return: 新向量
        """
        return Vector(tuple(x * times for x in self))

    @property
    def len(self):  # 模长
        """
        得到向量的模长
        @return: 向量的模长
        """
        return sqrt(sum(x ** 2 for x in self))

    def rotate(self, x, y, z):
        """
        旋转这个向量
        @param x: 绕x轴旋转弧度
        @param y: 绕y轴旋转弧度
        @param z: 绕z轴旋转弧度
        @return: 旋转后的向量
        """
        # 绕x轴
        new = (self[0],
               self[1] * cos(x) - self[2] * sin(x),
               self[1] * sin(x) + self[2] * cos(x))
        # 绕y轴
        new = (new[0] * cos(y) + new[2] * sin(y),
               new[1],
               new[2] * cos(y) - new[0] * sin(y))
        # 绕z轴
        new = (new[0] * cos(z) - new[1] * sin(z),
               new[0] * sin(z) + new[1] * cos(z),
               new[2])
        return Vector(new)

    def __add__(self, other):  # 加法
        """
        两个向量相加
        @param other: 另一个向量（可交换）
        @return: 和向量
        """
        return Vector(tuple(self[i] + other[i] for i in range(3)))

    def __sub__(self, other):  # 减法
        """
        两个向量相减
        @param other: 另一个向量（不可交换）
        @return: 差向量
        """
        return Vector(tuple(self[i] - other[i] for i in range(3)))

    def __mul__(self, other):  # 点乘
        """
        两个向量的点积（数量积）
        @param other: 另一个向量（可交换）
        @return: 向量的点积
        """
        return sum(self[i] * other[i] for i in range(3))

    def __pow__(self, other):  # 叉乘
        """
        两个向量的叉乘（向量积）
        @param other: 另一个向量（不可交换）
        @return: 叉乘得到的向量
        """
        ax, ay, az = self
        bx, by, bz = other
        return Vector((ay * bz - az * by, az * bx - ax * bz, ax * by - ay * bx))
