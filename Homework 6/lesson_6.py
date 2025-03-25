# 2. Реалізувати метод square в фігурах які залишилися. (Triangle+Parallelogram).
# Triangle - треба створити клас

import math as m


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.round = 2
        self.units = "cm"

    def __str__(self):
        return "Basic mathematic shape"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def area(self):
        return 0


class Circle(Shape):
    """Class used to represent a basic circle."""
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f"Circle with a radius of {self.radius} {self.units} and a center at ({self.x}, {self.y})."

    def area(self) -> float:
        """Calculate the area of a circle."""
        return round(m.pi * self.radius ** 2, self.round)

    def length(self) -> float:
        """Calculate the circumference (length) of a circle."""
        return round(2 * m.pi * self.radius, self.round)

    def contains(self, point: object) -> bool:
        """Checks if the passed point is inside the circle by comparing the distance between the points and the radius
        of the circle."""
        distance = m.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
        return distance <= self.radius


class Rectangle(Shape):
    """Class used to represent a basic rectangle."""
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def area(self) -> float:
        """Calculate the area of a rectangle."""
        return round(self.width * self.height, self.round)


class Parallelogram(Rectangle):
    """Class used to represent a basic parallelogram."""
    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def __str__(self):
        result = super().__str__()
        return result + (f" parallelogram: width = {self.width} {self.units}, height = {self.height} {self.units},"
                         f" angle = {self.angle} degrees.")

    def print_angle(self) -> None:
        """Display the angle of the parallelogram."""
        print(self.angle)

    def area(self) -> float:
        """Calculate the area of a parallelogram."""
        return round(self.width * self.height, self.round)


class Triangle(Shape):
    """Class used to represent a basic triangle."""
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def __str__(self):
        result = super().__str__()
        return result + f" triangle: width = {self.width} {self.units}, height = {self.height} {self.units}."

    def area(self) -> float:
        """Calculate the area of a triangle."""
        return round(0.5 * self.width * self.height, self.round)


class Point:
    """Class used to represent a basic point."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Scene:
    """Class used to store the created shapes and to display total area of all shapes."""
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_area(self):
        return sum(f.area() for f in self._figures)
