from pysics.render import Object3D, Surface3D
from pysics.maths import Coordinate
from pysics.maths.constants import world_origin, x_axis, y_axis


class Model(Object3D):
    
    """
    3D Models
    """
    
    def __init__(self, world, file, /, center=world_origin, x_dir=x_axis, y_dir=y_axis):
        """
        @param world: The world the model belongs to.
        @param file: The model file.
        @param center: The center of the model's coordinate. 
        @param x_dir: The x-axis of the model's coordinate. 
        @param y_dir: The y-axis of the model's coordinate.
        """
        super().__init__(world)
        self.coordinate = Coordinate(center, x_dir, y_dir)
        self.objects = list()
        # TODO Model file

