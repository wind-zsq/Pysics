from ..Render import *


class RigidBody3D:
    """
    3D刚体基类
    """

    def __init__(self, objects, center, mass, gravity=True, friction=0.0, elasticity=0.0):
        """
        创建一个3D刚体类
        :param objects: 物体（一个3D模型类）
        :param center: 物体的质心（重心）
        :param mass: 物体的质量
        :param gravity: 物体是否受重力
        :param friction: 物体的摩擦系数
        :param elasticity: 物体的弹性系数
        """
        self.objects = objects.to_group()
        self.center = center
        self.mass = mass
        self.gravity = gravity
        self.friction = friction
        self.elasticity = elasticity
        self.speed = Vec3D((0, 0, 0))

    def update(self):
        """
        每帧刷新物品
        """
        # gravity
        self.speed += Vec3D((0, 0, -2 * self.gravity))
        for each in self.objects:
            each.move(self.speed)


