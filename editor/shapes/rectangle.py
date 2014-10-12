from polyline import Polyline


class Rectangle(Polyline):
    """
    Store the state of a rectangle
    """

    header = 'R'

    def __init__(self, *args, **kargs):
        values = args[0]
        if len(values) is not 5:
            raise Exception('Wrong number of parameters')
        super(Rectangle, self).__init__(values)
