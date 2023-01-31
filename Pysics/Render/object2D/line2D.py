import pygame


from .object2D import *
from .point2D import *

class Line2D(Object2D):
    """
    2D线段类
    """
    def __init__(self, start, end, size=1, color=(0, 0, 0)):
        """
        创建一个2D线段
        :param start: 起点的坐标
        :param end: 终点的坐标
        :param size: 点的大小
        :param color: 点的颜色
        """
        self.start = Point2D(start, size, color)
        self.end = Point2D(end, size, color)
        self.size = size
        self.color = color

    def set_color(self, color):
        """
        设置线段的颜色
        :param color: 设置的颜色
        """
        self.color = color

    def to_screen(self, screen):
        """
        将坐标转换到屏幕上，以屏幕中心为原点
        :param screen: 绘制的屏幕
        :return: 转换后的屏幕坐标点
        """
        return Line2D(self.start.to_screen(screen).pos,
                      self.end.to_screen(screen).pos,
                      self.size, self.color)

    def update(self, screen):
        """
        每帧刷新绘制
        :param screen: 绘制的屏幕
        """
        pygame.draw.line(screen, self.color,
                         self.start.pos, self.end.pos, self.size)

