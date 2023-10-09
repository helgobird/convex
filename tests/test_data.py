from data import Data
from r2point import R2Point


class TestData:

    def test_init(self):
        p = Data()
        assert not p.FIRST_POINT and not p.SECOND_POINT

    def test_set_points(self):
        p = Data()
        Data.set_points(R2Point(0.0, 0.0), R2Point(1.0, 1.0))
        assert p.FIRST_POINT == R2Point(0.0, 0.0)
        assert p.SECOND_POINT == R2Point(1.0, 1.0)
        Data.set_points(R2Point(2.0, 2.0), R2Point(-1.0, -1.0))
        assert p.FIRST_POINT == R2Point(0.0, 0.0)
        assert p.SECOND_POINT == R2Point(1.0, 1.0)