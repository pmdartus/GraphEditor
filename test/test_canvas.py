from nose.tools import assert_equals, assert_raises
from editor.canvas import Canvas
from editor.shapes.circle import Circle
from editor.shapes.object_agregated import ObjectAgregated


class TestCanvas:
    def setup(self):
        self.canvas = Canvas()

    def test_add_element(self):
        self.canvas.add_element(Circle, 'circle1 2 3 1')
        self.canvas.add_element(Circle, 'circle2 2 3 1')
        self.canvas.add_element(ObjectAgregated, 'agg circle1 circle2')
        assert_equals(len(self.canvas.elem_store), 2)
        assert_equals(len(self.canvas.oa_store), 1)

    def test_add_element_with_existing_name(self):
        self.canvas.add_element(Circle, 'circle1 2 3 1')
        self.canvas.add_element(Circle, 'circle1 4 9 1')
        assert_equals(len(self.canvas.elem_store), 1)

    def test_add_element_with_existing_OA_name(self):
        self.canvas.add_element(Circle, 'circle1 2 3 1')
        self.canvas.add_element(Circle, 'circle2 4 9 1')
        self.canvas.add_element(ObjectAgregated, 'circle1 circle1 circle2')
        assert_equals(len(self.canvas.elem_store), 2)
        assert_equals(len(self.canvas.oa_store), 0)

    def test_add_element_with_incorrect_params(self):
        self.canvas.add_element(Circle, 'circle1 two 3 1')
        assert_equals(len(self.canvas.elem_store), 0)

    def test_clear_canvas(self):
        self.canvas.add_element(Circle, 'circle 2 3 1')
        self.canvas.add_element(Circle, 'circle2 2 3 1')
        assert_equals(len(self.canvas.elem_store), 2)
        self.canvas.clear()
        assert_equals(len(self.canvas.elem_store), 0)

    def test_clear_empty_canvas(self):
        self.canvas.clear()
        assert_equals(len(self.canvas.elem_store), 0)
