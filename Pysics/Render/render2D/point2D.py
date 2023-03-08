import pygame

from .object2D import *


class Point2D(Object2D):
    """
    2D点类
    """

    def __init__(self, pos, size = 1, color = (0, 0, 0)):
        """
        创建一个二2D点
        :param pos: 点的二维坐标
        :param size: 点绘制出来的半径（像素）
        :param color: 点绘制出来的颜色
        """
        self.pos = pos
        self.size = size
        self.color = color

    def set_color(self, color):
        """
        设置点的颜色
        :param color: 设置的颜色
        """
        self.color = color

    def to_screen(self, screen):
        """
        将坐标转换到屏幕上，以屏幕中心为原点
        :param screen: 绘制的屏幕
        :return: 转换后的屏幕坐标点
        """
        width = screen.get_width()
        height = screen.get_height()
        return Point2D((width / 2 + self.pos[0], height / 2 - self.pos[1]),
                       size = self.size, color = self.color)

    def update(self, screen):
        """
        每帧刷新绘制
        :param screen: 绘制的屏幕
        """
        pygame.draw.circle(screen, self.color, self.pos, self.size)

    def __getitem__(self, item):
        return self.pos[item]
