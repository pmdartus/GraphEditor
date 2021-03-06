from polyline import Polyline


class Line(Polyline):
    """
    Store the state of a line
    """

    header = 'L'

    def __init__(self, *args, **kargs):
        values = args[0]
        if len(values) is not 5:
            raise Exception('Wrong number of parameters')
        super(Line, self).__init__(values)
