import os
from nose.tools import assert_equals
from nose.plugins.skip import SkipTest
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

    def test_remove_element(self):
        self.canvas.add_element(Circle, 'circle1 2 3 1')
        self.canvas.add_element(Circle, 'circle2 2 3 1')
        assert_equals(len(self.canvas.elem_store), 2)
        self.canvas.remove_elements('circle2')
        assert_equals(len(self.canvas.elem_store), 1)

    def test_remove_unreferenced_element(self):
        self.canvas.add_element(Circle, 'circle1 2 3 1')
        self.canvas.add_element(Circle, 'circle2 2 3 1')
        assert_equals(len(self.canvas.elem_store), 2)
        self.canvas.remove_elements('foobar')
        assert_equals(len(self.canvas.elem_store), 2)

    def test_remove_nested_res(self):
        self.canvas.add_element(Circle, 'circle 2 3 1')
        self.canvas.add_element(Circle, 'circle2 2 3 1')
        self.canvas.add_element(ObjectAgregated, 'oa circle2')
        assert_equals(len(self.canvas.elem_store), 2)
        assert_equals(len(self.canvas.oa_store), 1)
        self.canvas.remove_elements('oa')
        assert_equals(len(self.canvas.elem_store), 1)
        assert_equals(len(self.canvas.oa_store), 0)

    def test_remove_remaining_references(self):
        self.canvas.add_element(Circle, 'circle1 2 3 1')
        self.canvas.add_element(Circle, 'circle2 2 3 1')
        self.canvas.add_element(ObjectAgregated, 'oa circle1 circle2')
        self.canvas.remove_elements('circle1')
        assert_equals(len(self.canvas.elem_store), 1)
        assert_equals(len(self.canvas.oa_store), 1)

    def test_remove_remaining_old_oa(self):
        self.canvas.add_element(Circle, 'circle1 2 3 1')
        self.canvas.add_element(ObjectAgregated, 'oa circle1')
        self.canvas.add_element(ObjectAgregated, 'oa2 circle1')
        self.canvas.remove_elements('circle1')
        assert_equals(len(self.canvas.elem_store), 0)
        assert_equals(len(self.canvas.oa_store), 0)

    def test_complexe_deletion(self):
        raise SkipTest
        self.canvas.add_element(Circle, 'circle1 2 3 1')
        self.canvas.add_element(ObjectAgregated, 'oa circle1')
        self.canvas.add_element(ObjectAgregated, 'oa2 oa')
        self.canvas.remove_elements('circle1')
        assert_equals(len(self.canvas.elem_store), 0)
        assert_equals(len(self.canvas.oa_store), 0)

    def test_list(self):
        ret = 'C circle1 2 3 1\nC foobar 2 3 1'
        self.canvas.add_element(Circle, 'foobar 2 3 1')
        self.canvas.add_element(Circle, 'circle1 2 3 1')
        assert_equals(self.canvas.list_elem(), ret)

    def test_clear_canvas(self):
        self.canvas.add_element(Circle, 'circle 2 3 1')
        self.canvas.add_element(Circle, 'circle2 2 3 1')
        assert_equals(len(self.canvas.elem_store), 2)
        self.canvas.clear()
        assert_equals(len(self.canvas.elem_store), 0)

    def test_clear_empty_canvas(self):
        self.canvas.clear()
        assert_equals(len(self.canvas.elem_store), 0)

    def test_save(self):
        filename = 'test.txt'
        ret = 'C circle2 2 3 1\nC circle1 2 3 1\nOA oa circle1'
        self.canvas.add_element(Circle, 'circle1 2 3 1')
        self.canvas.add_element(ObjectAgregated, 'oa circle1')
        self.canvas.add_element(Circle, 'circle2 2 3 1')
        try:
            self.canvas.save(filename)
            f = open(filename, 'r')
            assert_equals(f.read(), ret)
        finally:
            os.remove(filename)

    def test_load(self):
        filename = 'test.txt'
        ret = 'C circle2 2 3 1\nC circle1 2 3 1\nOA oa circle1'
        f = open(filename, 'w')
        f.write(ret)
        f.close()
        try:
            self.canvas.load(filename)
            assert_equals(len(self.canvas.elem_store), 2)
            assert_equals(len(self.canvas.oa_store), 1)
        finally:
            os.remove(filename)

    def test_move(self):
        self.canvas.add_element(Circle, 'circle 2 3 1')
        self.canvas.move('circle 1 3')
        assert_equals(self.canvas.elem_store['circle'].center.x, 3)
        assert_equals(self.canvas.elem_store['circle'].center.y, 6)

    def test_move_parsing_exception(self):
        self.canvas.add_element(Circle, 'circle 2 3 1')
        self.canvas.move('circle 1 two')
        assert_equals(self.canvas.elem_store['circle'].center.x, 2)
        assert_equals(self.canvas.elem_store['circle'].center.y, 3)

    def test_move_parsing_exception(self):
        self.canvas.add_element(Circle, 'circle 2 3 1')
        self.canvas.move('foo 1 2')
        assert_equals(self.canvas.elem_store['circle'].center.x, 2)
        assert_equals(self.canvas.elem_store['circle'].center.y, 3)
