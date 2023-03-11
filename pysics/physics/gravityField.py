import pysics.physics.field as field
import pysics.physics.force as force
import pysics.physics.physicalObject as physicalObject
import pysics.vector as vector


class GravityField(field.Field):
    """
    重力场类，可自定义重力方向与大小
    """

    def __init__(self, direct=(0, 0, -1)):
        """
        创建重力场
        @param direct: 重力场，默认竖直向下
        """
        self.direct = vector.Vector(direct)

    def update(self):
        # Gravity
        for each in physicalObject.physical_object_group:
            if each.gravity:
                each.add_force(force.Force(
                    self.direct,
                    each.center
                ))
