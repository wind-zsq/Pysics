import pysics.render.render2D as render2D
import pysics.vector as vector


class RenderObject:
    """
    所有3D对象的父类，用来标识3D对象
    """

    pass


class RenderObjectGroup:
    """
    3D对象容器类
    """

    def __init__(self):
        """
        创建一个空容器
        """
        self.__objects = list()

    @property
    def objects(self):
        """
        得到所有3D对象
        @return: 返回所有3D对象
        """
        return self.__objects

    def add(self, *obj):
        """
        向容器中添加对象
        @param obj: 添加的3D对象
        """
        for each in obj:
            if isinstance(each, RenderObject):
                self.__objects.append(each)

    def remove(self, *obj):
        """
        移除容器中对象
        @param obj: 移除的3D对象
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
        得到容器内3D对象的数量
        """
        return len(self.__objects)

    def __iter__(self):
        return iter(self.__objects)


class RenderPoint(RenderObject):
    """
    3D点类
    """

    def __init__(self, pos, size=2, color=(0, 0, 0), show=True):
        """
        创建一个3D点
        @param pos: 点的坐标
        @param size: 点的大小
        @param color: 点的颜色
        @param show: 是否显示
        """
        self.pos = pos
        self.size = size
        self.color = color
        self.show = show

    def move(self, direct):
        """
        将点沿向量移动
        @param direct: 一个向量，表示移动方向及距离
        @return: 移动后得到的点
        """
        self.__init__(tuple(self[i] + direct[i] for i in range(3)), size=self.size, color=self.color, show=self.show)
        return self

    def set_color(self, color):
        """
        给点设置颜色
        @param color: 设定的颜色
        """
        self.color = color

    def project(self, cam):
        """
        将世界中的Point3D转换到摄像机画面上
        @param cam: 选定摄像头
        @return: 转换后的Point2D，若点在摄像机后方则返回None
        """
        v_to = self - cam.pos
        dis = cam.direct * v_to + cam.angle / cam.len_pix
        if dis < 1 / cam.len_pix:
            return None
        scale = cam.len_pix / dis
        return render2D.Point2D(
            (cam.right * v_to * scale, cam.vert * v_to * scale),
            size=self.size,
            color=self.color
        ).to_screen(cam.screen)

    def __add__(self, other):
        """
        点与向量相加，得到新的点
        @param other: 另一个向量
        @return: 新的点
        """
        return RenderPoint(tuple(self[i] + other[i] for i in range(3)), size=self.size, color=self.color,
                           show=self.show)

    def __sub__(self, other):
        """
        将两个3D点类相减，得到一个向量
        @param other: 另一个3D点类
        @return: 两个点之间的向量
        """
        return vector.Vector(
            tuple(
                self[i] - other[i] for i in range(3)
            )
        )

    def __getitem__(self, item):
        return self.pos[item]


class RenderLine(RenderObject):
    """
    3D线段类
    """

    def __init__(self, start, end, size=2, color=(0, 0, 0), show=True):
        """
        创建一个3D线段
        @param start: 起点
        @param end: 终点
        @param size: 线段的粗细
        @param color: 线段的颜色
        @param show: 是否显示
        """
        self.start = RenderPoint(start, show=False)
        self.end = RenderPoint(end, show=False)
        self.size = size
        self.color = color
        self.show = show

    def move(self, direct):
        """
        将点沿向量移动
        @param direct: 一个向量，表示移动方向及距离
        @return: 移动后得到的点坐标
        """
        self.__init__(self.start.move(direct),
                      self.end.move(direct),
                      self.size, self.color, self.show)
        return self

    def set_color(self, color):
        """
        给点设置颜色
        @param color: 设定的颜色
        """
        self.color = color

    def project(self, cam):
        """
        将世界中的Line3D转换到摄像机画面上
        @param cam: 选定摄像头
        @return: 转换后的Line2D
        """
        out = (self.start.project(cam) is None) + (self.end.project(cam) is None)
        if out == 0:
            return render2D.Line2D(
                self.start.project(cam).pos,
                self.end.project(cam).pos,
                size=self.size,
                color=self.color
            )
        elif out == 2:
            return None
        else:
            try:
                front = (self.start
                         if self.end.project(cam) is None
                         else self.end)
                back = (self.end
                        if self.end.project(cam) is None
                        else self.start)
                v_line = vector.Vector(tuple(back.pos[i] - front.pos[i] for i in range(3)))
                v_to = front - cam.pos
                dis = cam.direct * v_to + cam.angle / cam.len_pix - 3 / cam.len_pix
                cross = front + v_line.to_len(dis)
                return render2D.Line2D(
                    cross.project(cam).pos,
                    front.project(cam).pos,
                    self.size, self.color
                )
            except:
                return None


class RenderSurface(RenderObject):
    """
    3D平面类
    """

    def __init__(self, points, color=(0, 0, 0), show=True, ):
        """
        创建一个3D平面
        @param points: 平面的3个顶点（元组）
        @param color: 平面的颜色
        @param show: 是否显示
        """
        self.points = tuple(RenderPoint(p, show=False) for p in points)
        self.color = color
        self.show = show

    def move(self, direct):
        """
        将点沿向量移动
        @param direct: 一个向量，表示移动方向及距离
        """
        for each in self.points:
            each.move(direct)

    def set_color(self, color):
        """
        给面设置颜色
        @param color: 设定的颜色
        """
        self.color = color

    def project(self, cam):
        """
        将世界中的Surface3D转换到摄像机画面上
        @param cam: 选定摄像头
        @return: 转换后的Surface2D
        """
        if (self.points[0].project(cam) is not None or
                self.points[1].project(cam) is not None or
                self.points[2].project(cam) is not None):
            return render2D.Surface2D(
                tuple(p.project(cam).pos for p in self.points),
                color=self.color
            )
        else:
            # TODO
            return None
