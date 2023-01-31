from math import *

from .Render import *

class Camera:
    """
    摄像机类，用于将视角画面投射到屏幕
    """

    def __init__(self, world, angle=45, sight=64):
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
        self.sight = sight

        self.pos = Point3D((0, 0, 0), show=False)
        self.direct = Vec3D((1, 0, 0))
        self.right = Vec3D((0, 1, 0))
        self.vert = self.direct ** self.right  # self.vert = Vec3D((0, 0, 1))

    def move(self, forward, right, vert):
        """
        移动摄像机（以相机为基准）
        :param forward: 向前移动
        :param right: 向右移动
        :param vert: 向上移动
        """
        self.pos = self.pos.move(self.direct.to_len(forward))
        self.pos = self.pos.move(self.right.to_len(right))
        self.pos = self.pos.move(Vec3D((0, 0, 1)).to_len(vert))

    def rotate(self, right, vert):
        """
        移动摄像机（以相机为基准）
        :param right: 向右转动
        :param vert: 向上转动
        """
        # self.direct += self.right.to_len(tan(right))
        # self.direct += self.vert.to_len(tan(vert))
        # self.direct = self.direct.to_len()
        # TODO

        # self.vert = self.direct ** self.right

    def point_project(self, point):
        """
        将世界中的Point3D转换到摄像机画面上
        :param point: 转换的Point3D
        :return: 转换后的Point2D，若点在摄像机后方则返回None
        """
        v_to = point - self.pos
        dis = self.direct * v_to + self.angle / self.len_pix
        if dis < 1 / self.len_pix:
            return None
        scale = self.len_pix / dis
        return Point2D((self.right * v_to * scale, self.vert * v_to * scale),
                       size=point.size, color=point.color).to_screen(self.screen)

    def line_project(self, line):
        """
        将世界中的Line3D转换到摄像机画面上
        :param line: 转换的Line3D
        :return: 转换后的Line2D
        """
        out = (self.point_project(line.start) is None) + (self.point_project(line.end) is None)
        if out == 0:
            return Line2D(self.point_project(line.start).pos,
                          self.point_project(line.end).pos,
                          size=line.size, color=line.color)
        elif out == 2:
            return None
        else:
            try:
                front = line.start if self.point_project(line.end) is None else line.end
                back = line.end if self.point_project(line.end) is None else line.start
                v_line = Vec3D(tuple(back.pos[i] - front.pos[i] for i in range(3)))
                v_to = front - self.pos
                dis = self.direct * v_to + self.angle / self.len_pix - 3 / self.len_pix
                cross = front + v_line.to_len(dis)
                return Line2D(self.point_project(cross).pos,
                              self.point_project(front).pos,
                              line.size, line.color)
            except:
                return None

    def surface_project(self, surf):
        """
        将世界中的Surface3D转换到摄像机画面上
        :param surf: 转换的Surface3D
        :return: 转换后的Surface2D
        """
        if (self.point_project(surf.points[0]) is not None or
                self.point_project(surf.points[1]) is not None or
                self.point_project(surf.points[2]) is not None):
            return Surface2D(tuple(self.point_project(p).pos for p in surf.points), color=surf.color)
        else:
            # TODO
            return None

    @property
    def len_pix(self):
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
            if each.show:
                points2D.add(self.point_project(each))
        points2D.update(self.screen)

        lines2D = Objects2D()
        for each in lines3D:
            if each.show:
                lines2D.add(self.line_project(each))
        lines2D.update(self.screen)

        surfaces2D = Objects2D()
        for each in surfaces3D:
            if each.show:
                surfaces2D.add(self.surface_project(each))
        surfaces2D.update(self.screen)

        models2D = Objects2D()
        for each in models3D:
            if each.show:
                models2D.add(self.point_project(p) for p in each.points)
                models2D.add(self.line_project(l) for l in each.lines)
                models2D.add(self.surface_project(s) for s in each.surfaces)
        models2D.update(self.screen)
