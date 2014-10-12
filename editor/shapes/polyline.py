from graphical_element import GraphicalElement
from point import Point


class Polyline(GraphicalElement):
    """
    Store information about a Polyline
    """
    def __init__(self, *args, **kargs):
        values = args[0]
        if len(values) % 2 == 0:
            raise Exception('Wrong number of parameters')
        super(Polyline, self).__init__(values[0])
        try:
            self.points = []
            coordinates = [int(i) for i in values[1:]]
            for i in xrange(0, len(coordinates), 2):
                self.points.append(Point(coordinates[i], coordinates[i+1]))
        except ValueError:
            raise Exception('Invalid argument')

    def __del__(self):
        has_points = hasattr(self, 'points')
        if has_points is not False:
            self.points[:] = []

    def __repr__(self):
        rep = 'PL {name} '.format(name=self.name)
        return rep + ' '.join([str(p) for p in self.points])

    def move(self, x, y):
        for p in self.points:
            p.move(x, y)
