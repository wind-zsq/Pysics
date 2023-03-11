import pysics.physics.physicalObject as physicalObject
import pysics.physics.surfaceField as surfaceField
import pysics.render.render3D as render3D


class PhysicalSurface(physicalObject.PhysicalObject):
    """
    物理物体外表面类
    """

    def __init__(self, points):
        """
        创建表面
        @param points: 3个顶点（元组），按逆时针决定法向量
        """
        self.points = tuple(render3D.RenderPoint(p) for p in points)
        self.center = render3D.RenderPoint(
            (
                (points[0][0] + points[1][0] + points[2][0]) / 3,
                (points[0][1] + points[1][1] + points[2][1]) / 3,
                (points[0][2] + points[1][2] + points[2][2]) / 3
            )
        )
        physicalObject.PhysicalObject.__init__(self, self.center, mass=0)

        # Normal vector of the surface
        self.normal = ((self.points[1] - self.points[0]) **
                       (self.points[2] - self.points[0])).to_len()

        self.collide = surfaceField.SurfaceField()

    def move(self):
        """
        移动平面
        """
        for each in self.points:
            each.move(self.linear_velocity)

    def rotate(self):
        """
        绕中心旋转平面
        """
        # TODO
        pass

    def update(self):
        """
        每帧刷新
        """
        self.linear_velocity += self.linear_acceleration
        self.angular_velocity += self.angular_acceleration
