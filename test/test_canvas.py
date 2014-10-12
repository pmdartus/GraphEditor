from nose.tools import assert_equals, assert_raises
from editor.canvas import Canvas
from editor.shapes.circle import Circle


class TestCanvas:
    def setup(self):
        self.canvas = Canvas()

    def test_clear_canvas(self):
        self.canvas.add_element(Circle, 'circle 2 3 1')
        self.canvas.add_element(Circle, 'circle2 2 3 1')
        assert_equals(len(self.canvas.elem_store), 2)
        self.canvas.clear()
        assert_equals(len(self.canvas.elem_store), 0)

    def test_clear_empty_canvas(self):
        self.canvas.clear()
        assert_equals(len(self.canvas.elem_store), 0)
