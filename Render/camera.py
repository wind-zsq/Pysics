from .object2D import *
from .object3D import *

from math import *

class Camera:
    def __init__(self, world, angle):
        """
        创建一个摄像机，每个World会自带一个
        :param world: 创建的世界
        :param angle: 摄像机视角
        """
        self.world = world
        self.screen = self.world.screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.angle = angle / 180 * pi

        self.pos = Point3D((0, 0, 0), add=False)
        self.direct = Vec3D((1, 0, 0))
        self.right = Vec3D((0, 1, 0))
        self.vert = self.direct ** self.right  # self.vert = Vec3D((0, 0, 1))

    def move(self, horizontal, vertical):
        """
        移动摄像机
        :param horizontal: 水平移动，以相机为基准（向右为正）
        :param vertical: 垂直移动，以标准坐标为基准（向上为正）
        """
        self.pos += self.right.toLen(horizontal)
        self.pos += Vec3D((0, 0, 1)).toLen(vertical)

    def rotate(self, x, y, z):
        """
        旋转摄像机，绕三个方向
        :param x: 绕x轴
        :param y: 绕y轴
        :param z: 绕z轴
        """
        self.direct = self.direct.rotate(x, y, z)
        self.right = self.right.rotate(x, y, z)
        self.vert = self.vert.vert(x, y, z)

    def pointTo2D(self, point):
        """
        将一个世界中的Point3D转换到摄像机画面上
        :param point: 转换的三维点
        :return: 转换后的二维点
        """
        v_to = point - self.pos
        dis = self.direct * v_to + self.angle / self.lenPix
        if dis < 1 / self.lenPix:
            return Point2D((self.width / 2, self.height / 2), size=point.size, color=point.color)
        scale = self.lenPix / dis
        return Point2D((self.right * v_to * scale, self.vert * v_to * scale),
                       size=point.size, color=point.color).toScreen(self.screen)

    @property
    def lenPix(self):
        """
        得到此摄像头1格等于几像素
        :return: 格与像素的比例关系
        """
        return self.width / 4 / tan(self.angle / 2)

    def show(self):
        """
        绘制摄像机拍摄画面
        """
        points2D = Objects2D()
        for each in points3D:
            pos = self.pointTo2D(each)
            points2D.add(pos)
        points2D.update(self.screen)
