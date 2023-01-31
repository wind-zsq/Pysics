from .point3D import *


class Line3D(Object3D):
    """
    3D线段类
    """

    def __init__(self, start, end, size=1, color=(0, 0, 0), show=True):
        """
        创建一个3D线段
        :param start: 起点
        :param end: 终点
        :param size: 线段的粗细
        :param color: 线段的颜色
        :param show: 是否加到线段集中
        """
        self.start = Point3D(start, show=False)
        self.end = Point3D(end, show=False)
        self.size = size
        self.color = color
        self.show = show
        lines3D.add(self)

    def move(self, direct):
        """
        将点沿向量移动
        :param direct: 一个向量，表示移动方向及距离
        :return: 移动后得到的点坐标
        """
        self = Line3D(self.start.move(direct),
                      self.end.move(direct),
                      self.size, self.color, self.show)
        return self

    def set_color(self, color):
        """
        给点设置颜色
        :param color: 设定的颜色
        """
        self.color = color


lines3D = Objects3D()
