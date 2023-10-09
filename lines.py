from functools import reduce
from r2point import R2Point
from math import inf, sqrt


def sign(n):  # функция для корректной работы метода __str__ класса Line
    return '+ ' + str(n) if n >= 0.0 else '- ' + str(-n)


def unique(lst):
    return list(reduce(lambda un, x: un + [x] if x not in un else un, lst, []))


class Line:
    """
    Класс Line
    Oбъект класса - прямая на плоскости, заданная
    тремя числами a, b, c - коэффициентами уравнения
    этой прямой a * x + b * y + c = 0 в выбранной
    системе координат.
    """

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    # Задание прямой двумя различными точками
    @staticmethod
    def sketch(p, q):
        return Line(q.y - p.y, p.x - q.x, p.y * q.x - p.x * q.y)

    # Пара чисел - коэффициенты в уравнении прямой y = k * x + b
    def special_case(self):
        return -self.a / self.b, -self.c / self.b

    # Параллельность прямой оси Oy
    def is_vertical(self):
        return self.b == 0

    # Пересечение двух прямых.
    # None - случай совпадения прямых;
    # R2Point(inf, inf) - случай параллельности,
    # остальные случаи стандартны.
    def intersect(self, other):
        det = self.a * other.b - self.b * other.a
        if det == 0:
            return (None if self.c * other.a == self.a * other.c
                    else R2Point(inf, inf))
        else:
            if self.is_vertical():
                x_coord = -self.c / self.a
                return R2Point(x_coord,
                               (-other.c - other.a * x_coord) / other.b)
            elif other.is_vertical():
                x_coord = -other.c / other.a
                return R2Point(x_coord,
                               (-self.c - self.a * x_coord) / self.b)
            else:
                sc_self, sc_oth = self.special_case(), other.special_case()
                x_coord = (sc_oth[1] - sc_self[1]) / (sc_self[0] - sc_oth[0])
                y_coord = sc_self[0] * x_coord + sc_self[1]
                return R2Point(x_coord, y_coord)

    # Пересечение с границей окна tkinter'а
    def intersection_with_canvas(self):
        upper_line = Line(0., 1., -6.)
        lower_line = Line(0., 1., 6)
        right_line = Line(1., 0., -6)
        left_line = Line(1., 0., 6)
        intersect_up = self.intersect(upper_line)
        intersect_lo = self.intersect(lower_line)
        intersect_ri = self.intersect(right_line)
        intersect_le = self.intersect(left_line)
        return list(filter(lambda p: R2Point.norm(p) <= 6.0 * sqrt(2),
                           unique([intersect_le, intersect_ri,
                                   intersect_lo, intersect_up])))

    # Прямые, ограничивающие 1-окрестность данной прямой
    def neighbourhood(self):
        return [Line(self.a, self.b, self.c + sqrt(self.b ** 2 + self.a ** 2)),
                Line(self.a, self.b, self.c - sqrt(self.b ** 2 + self.a ** 2))]

    def __str__(self):
        return f"{self.a} * x {sign(self.b)} * y {sign(self.c)} = 0.0"


if __name__ == '__main__':
    line = Line(0.0, 1.0, -1.0)
    neighbours = line.neighbourhood()
    for n in neighbours:
        print(n)
#    a, b, c = [float(s) for s in input().split()]
#   for line in Line(a, b, c).neighbourhood():
#        print(str(line))
