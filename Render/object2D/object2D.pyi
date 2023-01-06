from typing import Iterator
import pygame


class Object2D:
    """
    所有2D对象的父类，只用于标识2D对象
    """


class Objects2D:
    """
    用于包括2D对象的容器，进行集体绘制
    """

    def __init__(self):
        """
        创建一个2D容器
        """

    @property
    def objects(self) -> list:
        """
        得到容器中所有的对象
        :return: 列表，包括容器中所有2D对象
        """

    def add(self, *obj: Object2D) -> None:
        """
        向容器中添加2D对象，非2D对象不可加入
        :param obj: 可添加多个2D对象
        """

    def remove(self, *obj: Object2D) -> None:
        """
        从容器中移除指定2D对象
        :param obj: 可移除多个2D对象
        """

    def empty(self) -> None:
        """
        清空容器
        """

    def update(self, screen: pygame.surface.Surface):
        """
        对容器内所有2D对象执行update方法
        :param screen: 见每个2D对象的update方法
        """

    def __len__(self) -> int:
        """
        得到容器内对象的数量
        """

    def __iter__(self) -> Iterator:
        """
        返回容器的迭代器
        :return:容器的迭代器
        """
