import math
import re


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.magnitude = math.sqrt(self.x ** 2 + self.y ** 2)

    #def __get__(self):
        #ttuple = (self.x, self.y)
        #return ttuple

    def distance(self, point):
        x2 = point.x
        y2 = point.y
        return math.sqrt((y2-self.y)**2 + (x2-self.x)**2)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, num):
        x = self.x * num
        y = self.y * num
        return Point(x, y)
    # make (x * y = y * x)
    __rmul__ = __mul__

    def from_tuple(location=[0, 0]):
        list1 = list(location)
        return Point(list1[0], list1[1])

    def loc_from_tuple(self, location=[0, 0]):
        list1 = list(location)
        self.x = list1[0]
        self.y = list1[1]

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self):
        return f"Point at ({self.x}, {self.y})"


class Circle:
    """Class to create Circle objects"""

    def __init__(self, center=Point(0,0), radius=1):
        self.radius_log = []
        self.radius = radius
        self.center = center
        self.X = self.center.x
        self.Y = self.center.y

    def from_tuple(center=(0, 0), radius=1):
        list1 = list(center)
        center = Point(list1[0], list1[1])
        circle = Circle(center, radius)
        return circle

    def center_from_tuple(self, center=(0, 0)):
        list1 = list(center)
        self.center = Point(list1[0], list1[1])
        self.X = self.center.x
        self.Y = self.center.y


    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, center):
        if not isinstance(center,Point):
            raise ValueError("The center must be a Point")
        self._center = center

    @property
    def area(self):
        """Calculate and return the area of the Circle"""
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """Calculate and return the diameter of the Circle"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        """Set the diameter"""
        self.radius = diameter / 2

    @property
    def radius(self):
        """Return the actual radius value"""
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Set the radius value, checking validity and logging changes."""
        if radius < 0:
            raise ValueError("Radius cannot be negative!")
        self.radius_log.append(radius)
        self._radius = radius

    def __add__(self, other):
        return Circle(center=Point(self.X + other.X,
                      self.Y + other.Y),
                      radius=self.radius + other.radius)

    def __repr__(self):
        """Developer-friendly printing"""
        return f"Circle(center=Point({self.X}, {self.Y}), radius={self.radius})"

    def __str__(self):
        """User-friendly printing"""
        return f"Circle of radius {self.radius}"
