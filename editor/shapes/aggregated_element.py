from graphical_element import GraphicalElement


class AggregatedElement(GraphicalElement):
    """
    Describe a group of several objects
    """
    def __init__(self, *args, **kargs):
        values = args[0]
        if len(values) > 1:
            raise Exception('Wrong number of params')
        super(GraphicalElement, self).__init__(values[0])
        self
