from .vec3D import *
from .point3D import *
from .line3D import *
from .surface3D import *


class Model3D(Object3D):
    """
    3D模型类，可读取文件
    """

    def __init__(self, points=tuple(), lines=tuple(), surfaces=tuple(), show=True):
        """
        创建3D模型类
        """
        self.points = tuple(points)
        self.lines = tuple(lines)
        self.surfaces = tuple(surfaces)
        self.show = show
        models3D.add(self)
        if (not self.points) and (not self.lines) and (not self.surfaces):
            self.__get = False
        else:
            self.__get = True

    def get_file(self, file):
        """
        导入模型文件
        :param file: 模型文件
        :return: 导入后的3D模型
        """
        if not self.__get:
            f = open(file, "r")
            data = f.read()
            self.points = tuple(
                Point3D(*p) for p in eval(data.split("\n")[0]))
            self.lines = tuple(
                Line3D(*l) for l in eval(data.split("\n")[1]))
            self.surfaces = tuple(
                Surface3D(*s) for s in eval(data.split("\n")[2]))
        else:
            pass
        return self

    def to_file(self, file):
        """
        存储模型文件
        :param file: 模型文件名
        """
        try:
            points = [(p.pos, p.size, p.color, p.show) for p in self.points]
            lines = [(l.start.pos, l.end.pos, l.size, l.color, l.show) for l in self.lines]
            surfaces = [(tuple(p.pos for p in s.points), s.color, s.show) for s in self.surfaces]
            with open(file, "w") as f:
                f.write(f"{str(points)}\n{str(lines)}\n{str(surfaces)}")
        except:
            pass

    def to_group(self):
        group = Objects3D()
        group.add(*(Point3D(*p) for p in self.points),
                  *(Line3D(*l) for l in self.lines),
                  *(Surface3D(*s) for s in self.surfaces))
        return group

    def move(self, direct):
        """
        移动整个模型
        :param direct: 一个向量，表示移动方向及距离
        :return: 移动后的模型
        """
        points = []
        lines = []
        surfaces = []
        for each in self.points:
            points.append(each.move(direct))
        for each in self.lines:
            lines.append(each.move(direct))
        for each in self.surfaces:
            surfaces.append(each.move(direct))
        return Model3D(tuple(points), tuple(lines), tuple(surfaces))

models3D = Objects3D()