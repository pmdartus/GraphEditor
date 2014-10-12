from graphical_element import GraphicalElement
from point import Point


class Circle(GraphicalElement):
    """
    Store information about a Pircle
    """
    def __init__(self, *args, **kargs):
        values = args[0]
        if len(values) != 4:
            raise Exception('Wrong number of params')
        super(Circle, self).__init__(values[0])
        try:
            x = int(values[1])
            y = int(values[2])
            self.center = Point(x, y)
            radius = int(values[3])
            if radius < 0:
                raise Exception
            self.radius = radius
        except ValueError:
            raise Exception('Invalid argument')

    def __del__(self):
        has_center = hasattr(self, 'center')
        if has_center is not False:
            del self.center

    def __repr__(self):
        return "C {self.name} {self.center} {self.radius}".format(self=self)

    def move(slef, x, y):
        slef.center.move(x, y)
