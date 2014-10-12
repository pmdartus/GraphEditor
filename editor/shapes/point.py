class Point(object):
    """
    Store information about a Point
    """
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return "{self.x} {self.y}".format(self=self)

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
