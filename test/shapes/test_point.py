from nose.tools import assert_equals
from editor.shapes.point import Point


class TestPoint:
    def test_point_creation(self):
        p = Point(1, 2)
        assert_equals(p.x, 1)
        assert_equals(p.y, 2)

    def test_creation_with_no_int_values(self):
        p = Point(1, '2')
        assert_equals(p.y, 2)

    def test_move(self):
        p = Point(1, 2)
        p.move(-1, 1)
        assert_equals(p.x, 0)
        assert_equals(p.y, 3)

    def test_repr(self):
        p = Point(1, 2)
        assert_equals(str(p), '1 2')
