from Pysics import *


x, y, z = 0, 0, 0
p1 = (x, y, z)
p2 = (x, y, z + 2)
p3 = (x, y + 2, z)
p4 = (x, y + 2, z + 2)
p5 = (x + 2, y, z)
p6 = (x + 2, y, z + 2)
p7 = (x + 2, y + 2, z)
p8 = (x + 2, y + 2, z + 2)
points = Objects3D()
lines = Objects3D()
points.add(Point3D(p1, size=5))
points.add(Point3D(p2, size=5))
points.add(Point3D(p3, size=5))
points.add(Point3D(p4, size=5))
points.add(Point3D(p5, size=5))
points.add(Point3D(p6, size=5))
points.add(Point3D(p7, size=5))
points.add(Point3D(p8, size=5))
lines.add(Line3D(p1, p2, size=2))
lines.add(Line3D(p1, p3, size=2))
lines.add(Line3D(p4, p2, size=2))
lines.add(Line3D(p4, p3, size=2))
lines.add(Line3D(p5, p6, size=2))
lines.add(Line3D(p5, p7, size=2))
lines.add(Line3D(p8, p6, size=2))
lines.add(Line3D(p8, p7, size=2))
lines.add(Line3D(p1, p5, size=2))
lines.add(Line3D(p2, p6, size=2))
lines.add(Line3D(p3, p7, size=2))
lines.add(Line3D(p4, p8, size=2))
model = Model3D(tuple(points.objects), tuple(lines.objects))
model.to_file("cube.md3")

import math
p1 = Point3D((0, 2, 0))
p2 = Point3D((0, -2, 0))
p3 = Point3D((2 * math.sqrt(3), 0, 0))
p4 = Point3D((2 / math.sqrt(3), 0, 2 * math.sqrt(3)))
l1 = Line3D(p1.pos, p2.pos)
l2 = Line3D(p1.pos, p3.pos)
l3 = Line3D(p1.pos, p4.pos)
l4 = Line3D(p2.pos, p3.pos)
l5 = Line3D(p2.pos, p4.pos)
l6 = Line3D(p3.pos, p4.pos)
points = Objects3D()
lines = Objects3D()
points.add(p1)
points.add(p2)
points.add(p3)
points.add(p4)
lines.add(l1)
lines.add(l2)
lines.add(l3)
lines.add(l4)
lines.add(l5)
lines.add(l6)
model = Model3D(tuple(points.objects), tuple(lines.objects))
model.to_file("pyramid.md3")
