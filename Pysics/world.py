from .camera import *


class World:
    """
    世界类，创建世界以使用3D！
    """

    def __init__(self, screen, angle=45):
        """
        创建一个渲染3D世界，自带初始化摄像机
        :param screen: 创建在屏幕上
        :param angle: 摄像机视角，默认45度
        """
        self.screen = screen
        self.camera = Camera(self, angle)

        self.points2D = Object2D()

    def show(self):
        """
        在屏幕上显示摄像机视角
        """
        self.camera.show(self)


