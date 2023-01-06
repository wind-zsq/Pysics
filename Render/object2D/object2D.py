class Object2D:
    """
    所有2D对象的父类，只用于标识2D对象
    """
    pass


class Objects2D:
    """
    用于包括2D对象的容器，进行集体绘制
    """

    def __init__(self):
        """
        创建一个2D容器
        """
        self.__objects = list()

    @property
    def objects(self):
        """
        得到容器中所有的对象
        :return: 列表，包括容器中所有2D对象
        """
        return self.__objects

    def add(self, *obj):
        """
        向容器中添加2D对象，非2D对象不可加入
        :param obj: 可添加多个2D对象
        """
        for each in obj:
            if isinstance(each, Object2D):
                self.__objects.append(each)

    def remove(self, *obj):
        """
        从容器中移除指定2D对象
        :param obj: 可移除多个2D对象
        """
        for each in obj:
            self.__objects.remove(each)

    def empty(self):
        """
        清空容器
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
        得到容器内对象的数量
        """
        return len(self.__objects)

    def __iter__(self):
        """
        返回容器的迭代器
        :return:容器的迭代器
        """
        return iter(self.__objects)
