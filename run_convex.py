#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void
from data import Data


f = Void()
try:
    intro1 = "Координаты первой точки: "
    intro2 = "Координаты второй точки: "
    Data.FIRST_POINT = R2Point(*map(float,
                                    input(intro1).split()))
    Data.SECOND_POINT = R2Point(*map(float,
                                     input(intro2).split()))
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}, "
              f"N = {f.vertexes_number()}")
        print()
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    Data.reset_points()
