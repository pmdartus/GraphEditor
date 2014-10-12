from nose.tools import assert_equals, assert_raises
from editor.shapes.circle import Circle


class TestCircle:
    def test_circle_creation(self):
        c = Circle(['test_circle', '1', '3', '9'])
        assert_equals(c.name, 'test_circle')
        assert_equals(c.center.x, 1)
        assert_equals(c.center.y, 3)
        assert_equals(c.radius, 9)

    def test_creation_with_negative_values(self):
        c = Circle(['test_circle', '-1', '3', '9'])
        assert_equals(c.name, 'test_circle')
        assert_equals(c.center.x, -1)
        assert_equals(c.center.y, 3)
        assert_equals(c.radius, 9)

    def test_negative_radius(self):
        assert_raises(
            Exception,
            lambda: Circle(['test_circle', '-1', '3', '-9'])
        )

    def test_move(self):
        c = Circle(['test_circle', '1', '3', '9'])
        c.move(1, 5)
        assert_equals(c.center.x, 2)
        assert_equals(c.center.y, 8)
        assert_equals(c.radius, 9)

    def test_rep(self):
        c = Circle(['test_circle', '1', '3', '9'])
        rep = str(c)
        assert_equals(rep, 'C test_circle 1 3 9')
