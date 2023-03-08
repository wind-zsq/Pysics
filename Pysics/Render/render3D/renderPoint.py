from .renderObject import *
from .vector import *
from ..render2D import *


class RenderPoint(RenderObject):
    """
    3D点类
    """

    def __init__(self, pos, size = 2, color = (0, 0, 0), show = True):
        """
        创建一个3D点
        @param pos: 点的坐标
        @param size: 点的大小
        @param color: 点的颜色
        @param show: 是否显示
        """
        self.pos = pos
        self.size = size
        self.color = color
        self.show = show

    def move(self, direct):
        """
        将点沿向量移动
        @param direct: 一个向量，表示移动方向及距离
        @return: 移动后得到的点
        """
        self.__init__(tuple(self[i] + direct[i] for i in range(3)), size=self.size, color=self.color, show=self.show)
        return self

    def set_color(self, color):
        """
        给点设置颜色
        @param color: 设定的颜色
        """
        self.color = color

    def project(self, cam):
        """
        将世界中的Point3D转换到摄像机画面上
        @param cam: 选定摄像头
        @return: 转换后的Point2D，若点在摄像机后方则返回None
        """
        v_to = self - cam.pos
        dis = cam.direct * v_to + cam.angle / cam.len_pix
        if dis < 1 / cam.len_pix:
            return None
        scale = cam.len_pix / dis
        return Point2D(
            (cam.right * v_to * scale, cam.vert * v_to * scale),
            size = self.size,
            color = self.color
        ).to_screen(cam.screen)

    def __add__(self, other):
        """
        点与向量相加，得到新的点
        @param other: 另一个向量
        @return: 新的点
        """
        return RenderPoint(tuple(self[i] + other[i] for i in range(3)), size=self.size, color=self.color,
                           show=self.show)

    def __sub__(self, other):
        """
        将两个3D点类相减，得到一个向量
        @param other: 另一个3D点类
        @return: 两个点之间的向量
        """
        return Vector(
            tuple(
                self[i] - other[i] for i in range(3)
            )
        )

    def __getitem__(self, item):
        return self.pos[item]



