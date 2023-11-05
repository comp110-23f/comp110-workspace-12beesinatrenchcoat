"""Experimenting with the Point class."""
from lessons.CQ07.point import Point

p: Point = Point(2, 2)
print(p.x, p.y)
p.scale_by(8)
print(p.x, p.y)
p.scale(8)
q = p.scale(8)
print(p.x, p.y)
print(q.x, q.y)
