class Object3D:
    """
    所有3D对象的父类，用来标识3D对象
    """
    pass


class Objects3D:
    def __init__(self):
        self.__objects = list()

    @property
    def objects(self):
        return self.__objects

    def add(self, *obj):
        for each in obj:
            if isinstance(each, Object3D):
                self.__objects.append(each)

    def remove(self, *obj):
        for each in obj:
            self.__objects.remove(each)

    def empty(self):
        self.__objects = list()

    def __iter__(self):
        return iter(self.__objects)

