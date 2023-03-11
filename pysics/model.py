import pysics.render.render3D as render3D


class Model(render3D.RenderObject):
    """
    3D模型类，可读取文件
    """

    def __init__(self, *args):
        """
        创建3D模型类
        @param args: 导入模型文件(.md3)
        """
        if isinstance(args[0], str):
            f = open(args[0], "r")
            data = f.read()
            points = tuple(
                render3D.RenderPoint(*p) for p in eval(data.split("\n")[0]))
            lines = tuple(
                render3D.RenderLine(*l) for l in eval(data.split("\n")[1]))
            surfaces = tuple(
                render3D.RenderSurface(*s) for s in eval(data.split("\n")[2]))
            self.file = args[0]
            self.objects = (points, lines, surfaces)
        elif isinstance(args[0], render3D.RenderObjectGroup):
            points = []
            lines = []
            surfaces = []
            for each in args[0]:
                if isinstance(each, render3D.RenderPoint):
                    points.append(each)
                if isinstance(each, render3D.RenderLine):
                    lines.append(each)
                if isinstance(each, render3D.RenderSurface):
                    surfaces.append(each)
            self.objects = (tuple(points), tuple(lines), tuple(surfaces))

    def to_file(self, file):
        """
        存储模型文件
        @param file: 模型文件名
        """
        try:
            points = tuple((p.pos, p.size, p.color, p.show) for p in self.objects[0])
            lines = tuple((l.start.pos, l.end.pos, l.size, l.color, l.show) for l in self.objects[1])
            surfaces = tuple((tuple(p.pos for p in s.points), s.color, s.show) for s in self.objects[2])
            with open(file, "w") as f:
                f.write(f"{str(points)}\n{str(lines)}\n{str(surfaces)}")
        except:
            pass

    def to_group(self):
        group = render3D.RenderObjectGroup()
        group.add(*(render3D.RenderPoint(p.pos, p.size, p.color, p.show) for p in self.objects[0]),
                  *(render3D.RenderLine(*(l.start.pos, l.end.pos, l.size, l.color, l.show)) for l in self.objects[1]),
                  *(render3D.RenderSurface(*(tuple(p.pos for p in s.points), s.color, s.show)) for s in
                    self.objects[2]))
        return group

    def move(self, direct):
        """
        移动整个模型
        @param direct: 一个向量，表示移动方向及距离
        @return: 移动后的模型
        """
        objects = render3D.RenderObjectGroup()
        for each in self.objects[0]:
            objects.add(each.move(direct))
        for each in self.objects[1]:
            objects.add(each.move(direct))
        for each in self.objects[2]:
            objects.add(each.move(direct))
        return
