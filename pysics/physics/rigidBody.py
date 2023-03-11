import pysics.physics.physicalObject as physicalObject


class RigidBody3D(physicalObject.PhysicalObject):
    """
    3D刚体类
    """

    def __init__(self, world, objects, center, mass, gravity=True, friction=0.0, elasticity=0.0):
        """
        创建一个3D刚体类
        @param world: 物理世界
        @param objects: 物体（一个3D模型类）
        @param center: 物体的质心（重心）
        @param mass: 物体的质量
        @param gravity: 物体是否受重力
        @param friction: 物体的摩擦系数
        @param elasticity: 物体的弹性系数
        """
        physicalObject.PhysicalObject.__init__(self, world, center, mass, gravity)
        self.objects = objects.to_group()
        self.gravity = gravity
        self.friction = friction
        self.elasticity = elasticity

    def move(self):
        """
        移动物体
        """
        self.center.move(self.linear_velocity)
        for each in self.objects:
            each.move(self.linear_velocity)

    def rotate(self):
        """
        转动物体
        """
        # TODO
        pass

    def update(self):
        """
        每帧刷新
        """
        self.linear_velocity += self.linear_acceleration
        self.angular_velocity += self.angular_acceleration

        self.move()
        self.rotate()

        for each in self.objects:
            each.project(self.world.camera)
