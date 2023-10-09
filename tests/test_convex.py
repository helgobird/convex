from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon
from data import Data


class TestVoid:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Data.set_points(R2Point(0.0, 0.0), R2Point(1.0, 1.0))
        self.f = Void()

    # Нульугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Void (нульугольник)
    def test_void(self):
        assert isinstance(self.f, Void)

    # Периметр нульугольника нулевой
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    # Площадь нульугольника нулевая
    def test_area(self):
        assert self.f.area() == 0.0

    # Число вершин, удовлетворяющих условию задачи
    # у нульугольника нуль
    def test_vertexes_number(self):
        assert self.f.vertexes_number() == 0

    # При добавлении точки нульугольник превращается в одноугольник
    def test_add(self):
        assert isinstance(self.f.add(R2Point(0.0, 0.0)), Point)


class TestPoint:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Data.set_points(R2Point(0.0, 0.0), R2Point(1.0, 1.0))
        self.f = Point(R2Point(0.0, 0.0))

    # Одноугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Point (одноугольник)
    def test_point(self):
        assert isinstance(self.f, Point)

    # Периметр одноугольника нулевой
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    # Площадь одноугольника нулевая
    def test_area(self):
        assert self.f.area() == 0.0

    # self.f лежит в 1-окрестности заданной прямой
    def test_vertexes_number1(self):
        assert self.f.vertexes_number() == 1

    # Данная точка не лежит в 1-окрестности заданной прямой
    def test_vertexes_number2(self):
        p = Point(R2Point(0.0, 10.0))
        assert p.vertexes_number() == 0

    # Число вершин в окрестности увеличивается
    # при добавлении точки, лежащей в 1-окрестности заданной
    # прямой
    def test_vertexes_number3(self):
        assert self.f.add(R2Point(1.0, 1.0)).vertexes_number() == 2

    # Число вершин не изменяется при добавлении точки,
    # не лежащей в 1-окрестности заданной прямой
    def test_vertexes_number4(self):
        assert self.f.add(R2Point(0.0, 10.0)).vertexes_number() == 1

    # При добавлении точки одноугольник может не измениться
    def test_add1(self):
        assert self.f.add(R2Point(0.0, 0.0)) is self.f

    # При добавлении точки одноугольник может превратиться в двуугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(1.0, 0.0)), Segment)


class TestSegment:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Data.set_points(R2Point(0.0, 0.0), R2Point(1.0, 1.0))
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0))

    # Двуугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Segment (двуугольник)
    def test_segment(self):
        assert isinstance(self.f, Segment)

    # Периметр двуугольника равен удвоенной длине отрезка
    def test_perimeter(self):
        assert self.f.perimeter() == approx(2.0)

    # Площадь двуугольника нулевая
    def test_area(self):
        assert self.f.area() == 0.0

    # Число вершин в окрестности заданной прямой у self.f
    def test_vertexes_number1(self):
        assert self.f.vertexes_number() == 2

    # Число вершин в окрестности у заданного двуугольника
    def test_vertexes_number2(self):
        s = Segment(R2Point(0.0, 10.0), R2Point(10.0, 0.0))
        assert s.vertexes_number() == 0

    # При добавлении точки не из окрестности число вершин в
    # окрестности не увеличивается (фигура не изменилась)
    def test_vertexes_number3(self):
        assert self.f.add(R2Point(0.5, 0.0)).vertexes_number() == 2

    # При добавлении точки из окрестности число вершин в
    # окрестности увеличивается
    def test_vertexes_number4(self):
        assert self.f.add(R2Point(1.0, 1.0)).vertexes_number() == 3

    # При добавлении точки не из окрестности число вершин в
    # окрестности не увеличивается (двуугольник стал треугольником)
    def test_vertexes_number5(self):
        assert self.f.add(R2Point(0.0, 10.0)).vertexes_number() == 2

    # При добавлении точки двуугольник может не измениться
    def test_add1(self):
        assert self.f.add(R2Point(0.5, 0.0)) is self.f

    # При добавлении точки двуугольник может превратиться в другой двуугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(2.0, 0.0)), Segment)

    # При добавлении точки двуугольник может превратиться в треугольник
    def test_add3(self):
        assert isinstance(self.f.add(R2Point(0.0, 1.0)), Polygon)


class TestPolygon:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        Data.set_points(R2Point(0.0, 0.0), R2Point(1.0, 1.0))
        self.f = Polygon(
            R2Point(
                0.0, 0.0), R2Point(
                1.0, 0.0), R2Point(
                0.0, 1.0))

    # Многоугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Polygon (многоугольник)
    def test_polygon(self):
        assert isinstance(self.f, Polygon)

    # Изменение количества вершин многоугольника
    #   изначально их три
    def test_vertexes1(self):
        assert self.f.points.size() == 3
    #   добавление точки внутрь многоугольника не меняет их количества

    def test_vertexes2(self):
        assert self.f.add(R2Point(0.1, 0.1)).points.size() == 3
    #   добавление другой точки может изменить их количество

    def test_vertexes3(self):
        assert self.f.add(R2Point(1.0, 1.0)).points.size() == 4
    #   изменения выпуклой оболочки могут и уменьшать их количество

    def test_vertexes4(self):
        assert self.f.add(
            R2Point(
                0.4,
                1.0)).add(
            R2Point(
                1.0,
                0.4)).add(
                    R2Point(
                        0.8,
                        0.9)).add(
                            R2Point(
                                0.9,
                                0.8)).points.size() == 7
        assert self.f.add(R2Point(2.0, 2.0)).points.size() == 4

    # Изменение периметра многоугольника
    #   изначально он равен сумме длин сторон
    def test_perimeter1(self):
        assert self.f.perimeter() == approx(2.0 + sqrt(2.0))
    #   добавление точки может его изменить

    def test_perimeter2(self):
        assert self.f.add(R2Point(1.0, 1.0)).perimeter() == approx(4.0)

    # Изменение площади многоугольника
    #   изначально она равна (неориентированной) площади треугольника
    def test_area1(self):
        assert self.f.area() == approx(0.5)
    #   добавление точки может увеличить площадь

    def test_area2(self):
        assert self.f.add(R2Point(1.0, 1.0)).area() == approx(1.0)

    # Число вершин в окрестности у данного многоугольника
    def test_vertexes_number1(self):
        assert self.f.vertexes_number() == 3

    # При добавлении вершины внутрь выпуклой оболочки
    # число вершин в окрестности данной прямой не изменяется
    def test_vertexes_number2(self):
        assert self.f.add(R2Point(0.25, 0.25)).vertexes_number() == 3

    # При добавлении вершины из окрестности данной прямой
    # число вершин в окрестности данной прямой увеличивается
    def test_vertexes_number3(self):
        assert self.f.add(R2Point(1.0, 1.0)).vertexes_number() == 4

    # При добавлении вершины не из окрестности данной прямой
    # число вершин в окрестности данной прямой увеличивается
    def test_vertexes_number4(self):
        assert self.f.add(R2Point(1.0, 10.0)).vertexes_number() == 3
