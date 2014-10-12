from nose.tools import assert_equals, assert_raises
from editor.shapes.rectangle import Rectangle


class TestRectangle:
    def test_polyline_creation(self):
        r = Rectangle(['rect', '1', '3', '9', '2', '2', '2', '3', '4'])
        assert_equals(r.name, 'rect')
        assert_equals(len(r.points), 4)

    def test_wrong_nb_params(self):
        assert_raises(
            Exception,
            lambda: Rectangle(['rec', '1', '3'])
        )

    def test_repr(self):
        l = Rectangle(['rect', '1', '3', '9', '2', '2', '2', '3', '4'])
        assert_equals(str(l), 'R rect 1 3 9 2 2 2 3 4')
