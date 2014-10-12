from editor.command_parser import EditorPrompt
from editor.canvas import Canvas
from nose.tools import assert_equals


class TestCommandParser(object):
    def setup(self):
        self.canvas = Canvas()
        self.p = EditorPrompt(self.canvas)

    def test_command_circle(self):
        self.p.onecmd('C circle 1 1 1')
        assert_equals(len(self.canvas.elem_store), 1)
        assert_equals('circle' in self.canvas.elem_store, True)

    def test_command_line(self):
        self.p.onecmd('L line 1 1 1 3')
        assert_equals(len(self.canvas.elem_store), 1)
        assert_equals('line' in self.canvas.elem_store, True)

    def test_command_rectangle(self):
        self.p.onecmd('R rect 1 1 1 3')
        assert_equals(len(self.canvas.elem_store), 1)
        assert_equals('rect' in self.canvas.elem_store, True)

    def test_command_polyline(self):
        self.p.onecmd('PL polyline 1 1 1 3 4 5 7 8')
        assert_equals(len(self.canvas.elem_store), 1)
        assert_equals('polyline' in self.canvas.elem_store, True)

    def test_command_oa(self):
        self.p.onecmd('PL polyline 1 1 1 3 4 5 7 8')
        self.p.onecmd('OA oa polyline')
        assert_equals(len(self.canvas.oa_store), 1)
        assert_equals('oa' in self.canvas.oa_store, True)

    def test_command_list(self):
        self.p.onecmd('LIST')

    def test_command_clear(self):
        self.p.onecmd('C circle 1 1 1')
        self.p.onecmd('CLEAR')
        assert_equals(len(self.canvas.elem_store), 0)

    def test_command_move(self):
        self.p.onecmd('C circle 1 1 1')
        self.p.onecmd('MOVE circle 1 1')
        assert_equals(self.canvas.elem_store['circle'].center.x, 2)
        assert_equals(self.canvas.elem_store['circle'].center.y, 2)
