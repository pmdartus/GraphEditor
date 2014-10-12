from nose.tools import assert_equals, assert_raises
from editor.shapes.line import Line


class TestLine:
    def test_polyline_creation(self):
        l = Line(['line', '1', '3', '9', '2'])
        assert_equals(l.name, 'line')
        assert_equals(len(l.points), 2)
        assert_equals(l.points[0].x, 1)
        assert_equals(l.points[0].y, 3)
        assert_equals(l.points[1].x, 9)
        assert_equals(l.points[1].y, 2)

    def test_wrong_nb_params(self):
        assert_raises(
            Exception,
            lambda: Line(['line', '1', '3'])
        )

    def test_repr(self):
        l = Line(['line', '1', '3', '9', '2'])
        assert_equals(str(l), 'L line 1 3 9 2')
