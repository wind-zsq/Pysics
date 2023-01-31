from .point3D import *
from .line3D import *


class Surface3D(Object3D):
    """
    3D平面类
    """

    def __init__(self, points, color=(0, 0, 0), show=True, ):
        """
        创建一个3D平面
        :param points: 平面的顶点
        :param color: 线段的颜色
        :param show: 是否加到线段集中
        """
        self.points = tuple(Point3D(p, show=False) for p in points)
        v_1 = Vec3D(((points[0][0] - points[1][0]),
                     (points[0][1] - points[1][1]),
                     (points[0][2] - points[1][2])))
        v_2 = Vec3D(((points[0][0] - points[2][0]),
                     (points[0][1] - points[2][1]),
                     (points[0][2] - points[2][2])))
        self.direct = v_1 ** v_2
        self.color = color
        self.show = show
        surfaces3D.add(self)

    def move(self, direct):
        """
        将点沿向量移动
        :param direct: 一个向量，表示移动方向及距离
        :return: 移动后得到的点坐标
        """
        for each in self.points:
            each.move(direct)

    def set_color(self, color):
        """
        给点设置颜色
        :param color: 设定的颜色
        """
        self.color = color


surfaces3D = Objects3D()
