class Object3D:
    
    """
    3D Objects
    """
    def __init__(self, world):
        """
        @param world: The world the object belongs to.
        """
        self.world = world
        self.world.objects.append(self)
