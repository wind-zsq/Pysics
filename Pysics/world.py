from .Render import *
from .Physics import *
from .camera import *

import pygame


class World:
    """
    世界类，创建世界以使用3D！
    """

    def __init__(
            self,
            screen,
            angle = pi / 4,
            gravity_direct = (0, 0, -1),
            gravity_size = 5,
            fps = 50):
        """
        创建一个渲染3D世界，自带初始化摄像机
        @param screen: 创建在屏幕上
        @param angle: 摄像机视角，默认45度
        """
        self.screen = screen
        self.camera = Camera(self, angle)
        self.__fps = fps

        # Gravity
        self.gravity = GravityField(gravity_direct, gravity_size)

    def update(self):
        """
        刷新画面，此方法需被重复执行
        """
        self.camera.show()
        self.gravity.update()
        pygame.time.Clock().tick(self.__fps)
