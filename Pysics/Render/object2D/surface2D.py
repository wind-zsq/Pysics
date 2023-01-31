import pygame


from .object2D import *
from .point2D import *

class Surface2D(Object2D):
    """
    2D面类
    """

    def __init__(self, points, color=(0, 0, 0)):
        """
        创建一个2D线段
        :param points: 面的顶点
        :param color: 面的颜色
        """
        self.points = points
        self.color = color

    def set_color(self, color):
        """
        设置面的颜色
        :param color: 设置的颜色
        """
        self.color = color

    def to_screen(self, screen):
        """
        将坐标转换到屏幕上，以屏幕中心为原点
        :param screen: 绘制的屏幕
        :return: 转换后的屏幕坐标点
        """
        return Surface2D((p.to_screen(screen) for p in self.points), self.color)

    def update(self, screen):
        """
        每帧刷新绘制
        :param screen: 绘制的屏幕
        """
        pygame.draw.polygon(screen, self.color,
                            self.points, 0)

