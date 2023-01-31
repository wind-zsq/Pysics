from Pysics.Physics import *


class Object3D:
    """
    所有3D对象的父类，用来标识3D对象
    """

    pass


class Objects3D:
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
        :return: 返回所有3D对象
        """
        return self.__objects

    def add(self, *obj):
        """
        向容器中添加对象
        :param obj: 添加的3D对象
        """
        for each in obj:
            if isinstance(each, Object3D):
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

    def __len__(self):
        """
        得到容器内3D对象的数量
        """
        return len(self.__objects)

    def __iter__(self):
        return iter(self.__objects)
