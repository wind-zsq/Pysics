from .Render import *
from .Physics import *


class Camera:
    """
    摄像机类，用于将视角画面投射到屏幕
    """

    def __init__(self, world, angle = pi / 4, sight = 200):
        """
        创建一个摄像机，每个World会自带一个
        @param world: 创建的世界
        @param angle: 摄像机视角弧度
        """
        self.world = world
        self.screen = self.world.screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.angle = angle
        self.sight = sight

        self.pos = RenderPoint((0, 0, 0), show=False)
        self.direct = Vector((1, 0, 0))
        self.right = Vector((0, -1, 0))
        self.vert = self.right ** self.direct

    def move(self, forward, right, vert):
        """
        移动摄像机（以相机为基准）
        @param forward: 向前移动
        @param right: 向右移动
        @param vert: 向上移动
        """
        self.pos = self.pos.move(Vector((self.direct[0], self.direct[1], 0)).to_len(forward))
        self.pos = self.pos.move(self.right.to_len(right))
        self.pos = self.pos.move(Vector((0, 0, 1)).to_len(vert))

    def rotate_horizontal(self, right):
        """
        水平转动摄像机
        @param right: 向右转动弧度
        """
        self.direct = self.direct.rotate(0, 0, right).to_len()
        self.right = self.right.rotate(0, 0, right).to_len()
        self.vert = self.right ** self.direct

    def rotate_vertical(self, vert):
        """
        竖直转动摄相机
        @param vert: 向上转动弧度
        """
        angle = asin(self.direct[2])
        if angle + vert > pi / 2 or angle + vert < -pi / 2:
            pass
        else:
            self.direct = Vector((
                self.direct[0],
                self.direct[1],
                sqrt(self.direct[0] ** 2 + self.direct[1] ** 2) * tan(angle + vert)
            )).to_len()
            self.vert = self.right ** self.direct

    @property
    def len_pix(self):
        """
        得到此摄像头1格等于几像素
        :return: 格与像素的比例关系
        """
        return self.width / tan(self.angle / 2) / 4

    def show(self):
        """
        绘制摄像机拍摄画面
        """
        objects2D = Objects2D()
        for obj in physical_object_group:
            if (obj.center - self.pos).len <= self.sight:
                if hasattr(obj, "objects"):
                    for each in obj.objects:
                        objects2D.add(each.project(self))

        objects2D.update(self.screen)

