store = dict()


class Canvas(object):
    """
    Store canvas state
    """

    def addShape(shape):
        if shape.name in store:
            raise Exception('The shape name is already used')
        else:
            store[shape.name] = shape
