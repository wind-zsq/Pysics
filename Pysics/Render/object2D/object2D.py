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
