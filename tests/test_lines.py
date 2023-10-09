from pytest import approx
from lines import Line, sign
from r2point import R2Point
from math import inf


def r2approx(self, other):
    return (self.x == approx(other.x) and
            self.y == approx(other.y))


setattr(R2Point, 'approx', r2approx)


def line_approx(self, other):
    return (self.a == approx(other.a) and
            self.b == approx(other.b) and
            self.c == approx(other.c))


setattr(Line, 'approx', line_approx)


class TestLine:

    def test_sign1(self):
        assert sign(1.0) == '+ 1.0'

    def test_sign2(self):
        assert sign(-1.0) == '- 1.0'

    def test_sketch(self):
        p, q = R2Point(0.0, 0.0), R2Point(1.0, 1.0)
        line = Line.sketch(p, q)
        assert line.approx(Line(1.0, -1.0, 0.0))

    def test_special_case(self):
        line = Line(2.0, -2.0, 1.0)
        sc_line = line.special_case()
        assert (sc_line[0] == approx(1.0) and
                sc_line[1] == approx(0.5))

    def test_intersect1(self):
        line1 = Line(1.0, 1.0, 1.0)
        line2 = Line(2.0, 2.0, 2.0)
        assert not line1.intersect(line2)

    def test_intersect2(self):
        line1 = Line(1.0, 1.0, 1.0)
        line2 = Line(2.0, 2.0, 3.0)
        assert line1.intersect(line2) == R2Point(inf, inf)

    def test_intersect3(self):
        line1 = Line(1.0, 0.0, 1.0)
        line2 = Line(1.0, 1.0, 1.0)
        assert line1.intersect(line2).approx(R2Point(-1.0, 0.0))
        assert line2.intersect(line1).approx(R2Point(-1.0, 0.0))

    def test_intersect4(self):
        line1 = Line(2.0, 1.0, 4.0)
        line2 = Line(1.0, 1.0, -2.0)
        assert line1.intersect(line2).approx(R2Point(-6.0, 8.0))

    def test_intersect5(self):
        line1 = Line(0.5, -1.0, 2.0)
        line2 = Line(2.0, -1.0, -1.0)
        assert line1.intersect(line2).approx(R2Point(2.0, 3.0))

    def test_intersection_with_canvas1(self):
        line = Line.sketch(R2Point(7.0, 0.0), R2Point(8.0, 7.0))
        assert len(line.intersection_with_canvas()) == 0

    def test_intersection_with_canvas2(self):
        line = Line(1.0, -1.0, 0.0)
        points = line.intersection_with_canvas()
        assert any(x.approx(R2Point(-6.0, -6.0)) for x in points)
        assert any(x.approx(R2Point(6.0, 6.0)) for x in points)

    def test_intersection_with_canvas3(self):
        line = Line.sketch(R2Point(-6.0, -6.0), R2Point(6.0, 18.0))
        points = line.intersection_with_canvas()
        assert any(x.approx(R2Point(-6.0, -6.0)) for x in points)
        assert any(x.approx(R2Point(0.0, 6.0)) for x in points)

    def test_neighbourhood1(self):
        line = Line(0.0, 1.0, -1.0)
        neighbours = line.neighbourhood()
        assert neighbours[0].approx(Line(0.0, 1.0, 0.0))
        assert neighbours[1].approx(Line(0.0, 1.0, -2.0))

    def test_neighbourhood2(self):
        line = Line(1.0, 0.0, -1.0)
        neighbours = line.neighbourhood()
        assert neighbours[0].approx(Line(1.0, 0.0, 0.0))
        assert neighbours[1].approx(Line(1.0, 0.0, -2.0))

    def test_str(self):
        assert str(Line(1.0, 1.0, 1.0)) == "1.0 * x + 1.0 * y + 1.0 = 0.0"
        assert str(Line(2.0, -1.0, 3.0)) == "2.0 * x - 1.0 * y + 3.0 = 0.0"
        assert str(Line(-3.0, 1.0, -1.0)) == "-3.0 * x + 1.0 * y - 1.0 = 0.0"
