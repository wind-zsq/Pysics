import pygame


class World:
    def __init__(self, screen: pygame.surface.Surface, angle: int=45):
        """
        创建一个渲染3D世界，自带初始化摄像机
        :param screen: 创建在屏幕上
        :param angle: 摄像机视角，默认45度
        """

    def show(self) -> None:
        """
        在屏幕上显示摄像机视角
        """
