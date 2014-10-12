from nose.tools import assert_equals, assert_raises
from editor.shapes.polyline import Polyline


class TestPolyline:
    def test_polyline_creation(self):
        pl = Polyline(['polyline', '1', '3', '9', '2', '2', '9'])
        assert_equals(pl.name, 'polyline')
        assert_equals(len(pl.points), 3)
        assert_equals(pl.points[0].x, 1)
        assert_equals(pl.points[0].y, 3)
        assert_equals(pl.points[1].x, 9)
        assert_equals(pl.points[1].y, 2)
        assert_equals(pl.points[2].x, 2)
        assert_equals(pl.points[2].y, 9)

    def test_invalid_number_args_for_constrcutor(self):
        assert_raises(
            Exception,
            lambda: Polyline(['polyline', '1', '3', '9', '2', '2'])
        )

    def test_parse_error(self):
        assert_raises(
            Exception,
            lambda: Polyline(['polyline', 'one', '3', '9', '2', '2', '4'])
        )

    def test_move(self):
        pl = Polyline(['polyline', '1', '3', '9', '2', '2', '9'])
        pl.move(1, 2)
        assert_equals(pl.points[0].x, 2)
        assert_equals(pl.points[0].y, 5)
        assert_equals(pl.points[1].x, 10)
        assert_equals(pl.points[1].y, 4)
        assert_equals(pl.points[2].x, 3)
        assert_equals(pl.points[2].y, 11)

    def test_repr(self):
        pl = Polyline(['polyline', '1', '3', '9', '2', '2', '9'])
        assert_equals(str(pl), 'PL polyline 1 3 9 2 2 9')
