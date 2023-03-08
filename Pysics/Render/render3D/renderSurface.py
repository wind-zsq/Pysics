from .renderPoint import *
from .renderLine import *


class RenderSurface(RenderObject):
    """
    3D平面类
    """

    def __init__(self, points, color = (0, 0, 0), show = True, ):
        """
        创建一个3D平面
        @param points: 平面的3个顶点（元组）
        @param color: 平面的颜色
        @param show: 是否显示
        """
        self.points = tuple(RenderPoint(p, show = False) for p in points)
        self.color = color
        self.show = show

    def move(self, direct):
        """
        将点沿向量移动
        @param direct: 一个向量，表示移动方向及距离
        """
        for each in self.points:
            each.move(direct)

    def set_color(self, color):
        """
        给面设置颜色
        @param color: 设定的颜色
        """
        self.color = color

    def project(self, cam):
        """
        将世界中的Surface3D转换到摄像机画面上
        @param cam: 选定摄像头
        @return: 转换后的Surface2D
        """
        if (self.points[0].project(cam) is not None or
                self.points[1].project(cam) is not None or
                self.points[2].project(cam) is not None):
            return Surface2D(
                tuple(p.project(cam).pos for p in self.points),
                color = self.color
            )
        else:
            # TODO
            return None

