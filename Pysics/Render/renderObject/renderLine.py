from .renderPoint import *


class RenderLine(RenderObject):
    """
    3D线段类
    """

    def __init__(self, start, end, size = 2, color = (0, 0, 0), show = True):
        """
        创建一个3D线段
        @param start: 起点
        @param end: 终点
        @param size: 线段的粗细
        @param color: 线段的颜色
        @param show: 是否加到线段集中
        """
        self.start = RenderPoint(start, show=False)
        self.end = RenderPoint(end, show=False)
        self.size = size
        self.color = color
        self.show = show
        render_object_group.add(self)

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
            return Line2D(
                self.start.project(cam).pos,
                self.end.project(cam).pos,
                size = self.size,
                color = self.color
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
                v_line = Vector(tuple(back.pos[i] - front.pos[i] for i in range(3)))
                v_to = front - cam.pos
                dis = cam.direct * v_to + cam.angle / cam.len_pix - 3 / cam.len_pix
                cross = front + v_line.to_len(dis)
                return Line2D(
                    cross.project(cam).pos,
                    front.project(cam).pos,
                    self.size, self.color
                )
            except:
                return None

