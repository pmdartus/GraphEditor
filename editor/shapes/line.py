from polyline import Polyline


class Line(Polyline):
    """
    Store the state of a line
    """
    def __init__(self, *args, **kargs):
        values = args[0]
        if len(values) is not 5:
            raise Exception('Wrong number of parameters')
        super(Line, self).__init__(values)

    def __repr__(self):
        return "L {} {} {}".format(self.name, self.points[0], self.points[1])
