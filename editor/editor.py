from cmd import Cmd
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.line import Line
from shapes.polyline import Polyline
from shapes.object_agregated import ObjectAgregated
from canvas import Canvas

canvas = Canvas()


class EditorPrompt(Cmd):
    def do_C(self, args):
        """Create a circle and add it into the canvas"""
        canvas.add_element(Circle, args)

    def do_R(self, args):
        """Create a rectangle and add it into the canvas"""
        canvas.add_element(Rectangle, args)

    def do_L(self, args):
        """Create a line and add it into the canvas"""
        canvas.add_element(Line, args)

    def do_PL(self, args):
        """Create a polyline and add it into the canvas"""
        canvas.add_element(Polyline, args)

    def do_OA(self, args):
        """Create a object agregated and add it into the canvas"""
        canvas.add_element(ObjectAgregated, args)

    def do_LIST(self, arg):
        """List all the existing objects in the canvas"""
        canvas.list()

    def do_SAVE(self, arg):
        """Save the canvas in a file"""
        canvas.save(arg)

    def do_CLEAR(self, arg):
        """Empty the canvas"""
        canvas.clear()

    def do_EXIT(self, arg):
        """Exit program"""
        exit(0)

    def default(self, arg):
        """Handle unknow function"""
        print "Unknow command"


if __name__ == '__main__':
    prompt = EditorPrompt()
    prompt.prompt = '>'
    prompt.cmdloop('Welcome to Editor')
