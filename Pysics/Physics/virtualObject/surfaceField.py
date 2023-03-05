from ..physicalObject.physicalObject import *
from .field import *


class SurfaceField(Field):
    """
    物体表面的碰撞场类
    """

    def __init__(self, surface, center, friction = 0, elasticity = 0):
        """
        新建表面碰撞场
        @param surface: 物体表面
        @param center: 表面中心
        @param friction: 表面摩擦系数
        @param elasticity: 表面弹性系数
        """

        self.surface = surface
        self.center = center
        self.friction = friction
        self.elasticity = elasticity

    def update(self):
        """
        每帧刷新
        """
        # TODO
        for each in physical_object_group:
            pass
