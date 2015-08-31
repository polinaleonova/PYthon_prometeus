__author__ = 'polina'

import math

class Sphere(object):

    def __init__(self, rad = 1, x0 = 0.0, y0 = 0.0, z0 = 0.0):
        self.rad = rad
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0

    def  get_volume(self):
        self.volume = (4*math.pi*self.rad**3)/3
        return self.volume

    def get_square(self):
        self.square = 4*math.pi*(self.rad**2)
        return self.square

    def get_radius(self):
        return self.rad

    def get_center(self):
        return (self.x0,self.y0,self.z0)

    def set_radius(self, r):
        self.rad = r

    def set_center(self, x, y, z):
        self.x0 =x
        self.y0 =y
        self.z0 =z

    def is_point_inside(self, x, y, z):
        return (self.x0-x)**2+(self.y0-y)**2+(self.z0-z)**2<=(self.rad)**2




s1 = Sphere()
# print s0.rad
# print s1.get_center()
print s1.set_center(0.5, 1, 0)
# print s1.get_volume()
print s1.is_point_inside(0, 0, 0.99)
s1.set_radius(1.1)
# print s1.is_point_inside(0, -1.5, 0)
# print s1.get_radius()
# print s1.get_square()

import math


# proposed:
# class Sphere(object):
#     center = {'x':0, 'y':0, 'z':0}
#     radius = 1
#
#     def __init__(self, r = 1, x = 0, y = 0, z = 0):
#         self.set_radius(r)
#         self.set_center(x, y, z)
#
#     def get_volume(self):
#         return 4.0 / 3 * math.pi * self.radius ** 3
#
#     def get_square(self):
#         return 4.0 * math.pi * self.radius ** 2
#
#     def set_radius(self, r):
#         self.radius = r
#
#     def set_center(self, x = 0, y = 0, z = 0):
#         self.center['x'] = x
#         self.center['y'] = y
#         self.center['z'] = z
#
#     def get_radius(self):
#         return self.radius * 1.0
#
#     def get_center(self):
#         return (self.center['x'] * 1.0, self.center['y'] * 1.0, self.center['z'] * 1.0)
#
#     def is_point_inside(self, x = 0, y = 0, z = 0):
#         distance = math.sqrt((self.center['x'] - x)**2 +
#                             (self.center['y'] - y)**2 +
#                             (self.center['z'] - z)**2)
#         return distance < self.radius