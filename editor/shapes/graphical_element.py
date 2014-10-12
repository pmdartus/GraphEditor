class GraphicalElement(object):
    """
    Abstract class to store the state of an element
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        raise NotImplementedError

    def move(self, x, y):
        raise NotImplementedError
