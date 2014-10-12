from shapes.object_agregated import ObjectAgregated


class Canvas(object):
    """
    Hold informations concerning a Canvas
    """
    def __init__(self):
        self.elem_store = dict()
        self.oa_store = dict()

    def is_name_used(self, name):
        """Return boolean is the name is used or not"""
        return name in self.elem_store or name in self.oa_store

    def add_element(self, constructor, args):
        """Create the element via contructor and store it in the canvas"""
        args = args.split(' ')
        try:
            obj = constructor(args)
            if isinstance(obj, ObjectAgregated):
                self.add_agregated_object(obj)
            else:
                self.add_shape(obj)
        except Exception, e:
            print "ERR\n#{msg}".format(msg=e.message)
        else:
            print "OK\n#New object: {obj}".format(obj=obj)

    def add_shape(self, shape):
        """Add a shape in the canvas"""
        if Canvas.is_name_used(shape.name):
            raise Exception('The shape name is already used')
        self.elem_store[shape.name] = shape

    def add_agregated_object(self, obj):
        """Add an agregated object in the canvas"""
        if Canvas.is_name_used(obj.name):
            raise Exception('The shape name is already used')
        for ref in obj.shapes:
            if not Canvas.is_name_used(ref):
                raise Exception('Unknown reference: {}'.format(ref))
        self.oa_store[obj.name] = obj

    def list(self):
        """List existing shapes and agregated objects"""
        elems = self.elem_store.copy()
        elems.update(self.oa_store)
        names = elems.keys()
        for k in sorted(names):
            print elems[k]

    def clear(self):
        """Call `_clear_canvas`"""
        Canvas._clear_canvas()
        print 'OK'

    def remove_elements(self, args):
        """Remove the passed elements from the canvas"""
        try:
            for elem in args.split(' '):
                self._remove_element(elem)
        except Exception, e:
            print "ERR\n#{msg}".format(msg=e.message)
        else:
            print 'OK'

    def _clear_canvas(self):
        """Remove all the existing shapes and objects"""
        self.elem_store.clear()
        self.oa_store.clear()

    def _remove_element(self, name):
        """Remove recursively all the needed elements"""
        if name in self.elem_store:
            del self.elem_store[name]
        elif name in self.oa_store:
            for elem in self.oa_store[name]:
                self._remove_element(elem)
        else:
            raise Exception('Unknown reference')
