#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon
from data import Data


def void_draw(self, tk):
    pass


def point_draw(self, tk, points):
    tk.draw_point(self.p)
    tk.draw_neighbourhood(*points)


def segment_draw(self, tk, points):
    tk.draw_line(self.p, self.q)
    tk.draw_neighbourhood(*points)


def polygon_draw(self, tk, points):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())
    tk.draw_neighbourhood(*points)


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
f = Void()
tk.clean()

try:
    intro1 = "Координаты первой точки: "
    intro2 = "Координаты второй точки: "
    Data.FIRST_POINT = R2Point(*map(float,
                                    input(intro1).split()))
    Data.SECOND_POINT = R2Point(*map(float,
                                     input(intro2).split()))
    tk.draw_neighbourhood(Data.FIRST_POINT, Data.SECOND_POINT)
    while True:
        f = f.add(R2Point())
        tk.clean()
        f.draw(tk, [Data.FIRST_POINT, Data.SECOND_POINT])
        print(f"S = {f.area()}, P = {f.perimeter()}, "
              f"N = {f.vertexes_number()}\n")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
