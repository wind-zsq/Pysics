from .object2D import *
from .object3D import *
from .world import *


class Camera:
    def __init__(self, world: World, angle: int):
        """
        创建一个摄像机，每个World会自带一个
        :param world: 创建的世界
        :param angle: 摄像机视角
        """

    def move(self, horizontal: float, vertical: float) -> None:
        """
        移动摄像机
        :param horizontal: 水平移动，以相机为基准（向右为正）
        :param vertical: 垂直移动，以标准坐标为基准（向上为正）
        """

    def rotate(self, x: int, y: int, z: int) -> None:
        """
        旋转摄像机，绕三个方向
        :param x: 绕x轴
        :param y: 绕y轴
        :param z: 绕z轴
        """

    def pointTo2D(self, point) -> Point2D:
        """
        将一个世界中的Point3D转换到摄像机画面上
        :param point: 转换的三维点
        :return: 转换后的二维点
        """

    @property
    def lenPix(self) -> float:
        """
        得到此摄像头1格等于几像素
        :return: 格与像素的比例关系
        """

    def show(self) -> None:
        """
        绘制摄像机拍摄画面
        """
