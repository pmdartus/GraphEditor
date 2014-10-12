from nose.tools import assert_equals, assert_raises
from editor.shapes.object_agregated import ObjectAgregated


class TestObjectAgregated:
    def test_polyline_creation(self):
        oa = ObjectAgregated(['oa', 'circle', 'rect'])
        assert_equals(oa.name, 'oa')
        assert_equals(len(oa.shapes), 2)
        assert_equals(oa.shapes[0], 'circle')
        assert_equals(oa.shapes[1], 'rect')

    def test_wrong_nb_params(self):
        assert_raises(
            Exception,
            lambda: ObjectAgregated(['oa'])
        )

    def test_repr(self):
        oa = ObjectAgregated(['oa', 'circle', 'rect'])
        assert_equals(str(oa), 'OA oa circle rect')
