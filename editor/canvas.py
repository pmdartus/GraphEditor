from shapes.object_agregated import ObjectAgregated
from command_parser import EditorPrompt


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
                self._add_agregated_object(obj)
            else:
                self._add_shape(obj)
        except Exception, e:
            print "ERR\n#{msg}".format(msg=e.message)
        else:
            print "OK\n#New object: {obj}".format(obj=obj)

    def _add_shape(self, shape):
        """Add a shape in the canvas"""
        if self.is_name_used(shape.name):
            raise Exception('The shape name is already used')
        self.elem_store[shape.name] = shape

    def _add_agregated_object(self, obj):
        """Add an agregated object in the canvas"""
        if self.is_name_used(obj.name):
            raise Exception('The shape name is already used')
        for ref in obj.shapes:
            if not self.is_name_used(ref):
                raise Exception('Unknown reference: {}'.format(ref))
        self.oa_store[obj.name] = obj

    def list(self):
        """List existing shapes and agregated objects"""
        print self.list_elem()

    def list_elem(self):
        elems = self.elem_store.copy()
        elems.update(self.oa_store)
        names = sorted(elems.keys())
        return '\n'.join([str(elems[name]) for name in names])

    def clear(self):
        """Call `_clear_canvas`"""
        self._clear_canvas()
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
            self._remove_element_references(name)
            del self.elem_store[name]
        elif name in self.oa_store:
            referenced_items = self.oa_store[name]
            for elem in referenced_items.shapes:
                self._remove_element_references(name)
                self._remove_element(elem)
            del self.oa_store[name]
        else:
            raise Exception('Unknown reference')

    def _remove_element_references(self, name):
        """Remove in all the OA the referenced items"""
        oa_to_delete = []
        for key, group in self.oa_store.iteritems():
            if name in group.shapes:
                group.shapes.remove(name)
            if len(group.shapes) == 0:
                oa_to_delete.append(key)
        for key in oa_to_delete:
            del self.oa_store[key]

    def save(self, filename):
        """Save current canvas into a file"""
        f = open(filename, "w")
        ret = '\n'.join([str(elem) for elem in self.elem_store.itervalues()])
        ret += '\n'
        ret += '\n'.join([str(elem) for elem in self.oa_store.itervalues()])
        f.write(ret)
        f.close()

    def load(self, filename):
        """Load in memory the file"""
        self.clear()
        f = open(filename, "r")
        commands = f.read().split('\n')
        print commands
        prompt = EditorPrompt(self)
        for cmd in commands:
            prompt.onecmd(cmd)
