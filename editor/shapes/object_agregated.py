from graphical_element import GraphicalElement


class ObjectAgregated(GraphicalElement):
    """
    Describe a group of several objects
    """
    def __init__(self, *args, **kargs):
        values = args[0]
        if len(values) < 2:
            raise Exception('Wrong number of params')
        super(ObjectAgregated, self).__init__(values[0])
        self.shapes = values[1:]

    def __repr__(self):
        rep = 'OA {name} '.format(name=self.name)
        return rep + ' '.join(self.shapes)
