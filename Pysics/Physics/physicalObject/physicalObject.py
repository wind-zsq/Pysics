from ...Render import *


class PhysicalObject:
    """
    物理物体基类，仅用于标识物理物体
    """

    def __init__(self, center, mass, gravity = True):
        """
        创建新的物理物体
        :param center: 物体的质心
        :param mass: 物体的质量
        """
        self.center = RenderPoint(center, show=False)
        self.mass = mass
        self.gravity = gravity

        self.linear_velocity = Vector((0, 0, 0))
        self.linear_acceleration = Vector((0, 0, 0))
        self.angular_velocity = Vector((0, 0, 0))
        self.angular_acceleration = Vector((0, 0, 0))

        physical_object_group.add(self)

    def add_force(self, force):
        """
        给物体施加力
        :param force: 施加的力
        """
        self.linear_acceleration += force.direct * (1 / self.mass)
        # Calculated moment
        v_center_point = force.point - self.center
        d_center_force = v_center_point * force.direct * len(v_center_point)
        self.angular_acceleration += force.direct * d_center_force / self.mass
        # TODO

    def move(self):
        """
        移动物体方法，需要在不同的子类被重写
        """
        pass

    def rotate(self):
        """
        转动物体方法，需要在不同的子类被重写
        """
        pass

    def update(self):
        """
        每帧刷新方法，需要在不同的子类被重写
        """
        pass


class PhysicalObjectGroup:
    """
    物理物体容器类
    """

    def __init__(self):
        """
        创建一个空容器
        """
        self.__objects = list()

    @property
    def objects(self):
        """
        得到所有物理对象
        :return: 返回所有物理对象
        """
        return self.__objects

    def add(self, *obj):
        """
        向容器中添加对象
        :param obj: 添加的物理对象
        """
        for each in obj:
            if isinstance(each, PhysicalObject):
                self.__objects.append(each)

    def remove(self, *obj):
        """
        移除容器中对象
        :param obj: 移除的物理对象
        """
        for each in obj:
            self.__objects.remove(each)

    def empty(self):
        """
        清空容器所有对象
        """
        self.__objects = list()

    def __len__(self):
        """
        得到容器内物理对象的数量
        """
        return len(self.__objects)

    def __iter__(self):
        return iter(self.__objects)


physical_object_group = PhysicalObjectGroup()