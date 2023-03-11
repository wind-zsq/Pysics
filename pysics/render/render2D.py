import pygame


class Object2D:
    """
    所有2D对象的父类，只用于标识2D对象
    """

    pass


class Objects2D:
    """
    2D对象的容器类
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
        :return: 返回所有3D对象
        """
        return self.__objects

    def add(self, *obj):
        """
        向容器中添加对象
        :param obj: 添加的3D对象
        """
        for each in obj:
            if isinstance(each, Object2D):
                self.__objects.append(each)

    def remove(self, *obj):
        """
        移除容器中对象
        :param obj: 移除的3D对象
        """
        for each in obj:
            self.__objects.remove(each)

    def empty(self):
        """
        清空容器所有对象
        """
        self.__objects = list()

    def update(self, screen):
        """
        对容器内所有2D对象执行update方法
        :param screen: 见每个2D对象的update方法
        """
        for each in self.__objects:
            each.update(screen)

    def __len__(self):
        """
        得到容器内2D对象的数量
        """
        return len(self.__objects)

    def __iter__(self):
        return iter(self.__objects)


class Point2D(Object2D):
    """
    2D点类
    """

    def __init__(self, pos, size=1, color=(0, 0, 0)):
        """
        创建一个二2D点
        :param pos: 点的二维坐标
        :param size: 点绘制出来的半径（像素）
        :param color: 点绘制出来的颜色
        """
        self.pos = pos
        self.size = size
        self.color = color

    def set_color(self, color):
        """
        设置点的颜色
        :param color: 设置的颜色
        """
        self.color = color

    def to_screen(self, screen):
        """
        将坐标转换到屏幕上，以屏幕中心为原点
        :param screen: 绘制的屏幕
        :return: 转换后的屏幕坐标点
        """
        width = screen.get_width()
        height = screen.get_height()
        return Point2D((width / 2 + self.pos[0], height / 2 - self.pos[1]),
                       size=self.size, color=self.color)

    def update(self, screen):
        """
        每帧刷新绘制
        :param screen: 绘制的屏幕
        """
        pygame.draw.circle(screen, self.color, self.pos, self.size)

    def __getitem__(self, item):
        return self.pos[item]


class Line2D(Object2D):
    """
    2D线段类
    """

    def __init__(self, start, end, size=1, color=(0, 0, 0)):
        """
        创建一个2D线段
        :param start: 起点的坐标
        :param end: 终点的坐标
        :param size: 点的大小
        :param color: 点的颜色
        """
        self.start = Point2D(start, size, color)
        self.end = Point2D(end, size, color)
        self.size = size
        self.color = color

    def set_color(self, color):
        """
        设置线段的颜色
        :param color: 设置的颜色
        """
        self.color = color

    def to_screen(self, screen):
        """
        将坐标转换到屏幕上，以屏幕中心为原点
        :param screen: 绘制的屏幕
        :return: 转换后的屏幕坐标点
        """
        return Line2D(self.start.to_screen(screen).pos,
                      self.end.to_screen(screen).pos,
                      self.size, self.color)

    def update(self, screen):
        """
        每帧刷新绘制
        :param screen: 绘制的屏幕
        """
        pygame.draw.line(screen, self.color,
                         self.start.pos, self.end.pos, self.size)

class Surface2D(Object2D):
    """
    2D面类
    """

    def __init__(self, points, color=(0, 0, 0)):
        """
        创建一个2D线段
        :param points: 面的顶点
        :param color: 面的颜色
        """
        self.points = points
        self.color = color

    def set_color(self, color):
        """
        设置面的颜色
        :param color: 设置的颜色
        """
        self.color = color

    def to_screen(self, screen):
        """
        将坐标转换到屏幕上，以屏幕中心为原点
        :param screen: 绘制的屏幕
        :return: 转换后的屏幕坐标点
        """
        return Surface2D((p.to_screen(screen) for p in self.points), self.color)

    def update(self, screen):
        """
        每帧刷新绘制
        :param screen: 绘制的屏幕
        """
        pygame.draw.polygon(screen, self.color,
                            self.points, 0)