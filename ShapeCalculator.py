import math

class Shape:
    """Main parent class"""
    titele = "Фигура"

    def __init__(self):
        pass

    def area(self):
        pass

    def perimetr(self):
        pass

class PlaneShapes(Shape):
    titele = "Плоские Фигуры"

    def __init__(self):
        super().__init__()

class VolumetricShapes(Shape):
    titele = "Объемные Фигура"

    def __init__(self):
        super().__init__()

    def volume(self):
        pass

class Square(PlaneShapes):
    titele = "Квадрат"

    def __init__(self, x):
        super().__init__()
        self.x = x

    def area(self):
        return self.x ** 2

    def perimetr(self):
        return self.x * 4


class Rectangle(Square):
    titele = "Прямоугольник"

    def __init__(self, x, y):
        super(Square, self).__init__()
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimetr(self):
        return (2 * self.x) + (2 * self.y)

class Circle(PlaneShapes):
    titele = "Круг"

    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        return (self.r ** 2) * math.pi

    def circumference(self):
        return self.r * 2 * math.pi

    def diametr(self):
        return self.r * 2

class Triangle(PlaneShapes):
    titele = "Равносторонний Треугольник"

    def __init__(self, x):  #
        super().__init__()
        self.x = x             # Сторона
        self.h = math.sqrt(self.x ** 2 - (self.x ** 2)/4)

    def height(self):
        return self.h

    def area(self):
        return (self.x * self.h) / 2

    def median(self):
        return (math.sqrt(3) * self.x)/2

class Rombus(PlaneShapes):
    titele = "Ромб"

    def __init__(self, a, b, c, d):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.diag1 = math.sqrt(a ** 2 + b ** 2)
        self.diag2 = math.sqrt(c ** 2 + d ** 2)

    def area(self):
        return (self.diag1 * self.diag2) / 2

    def perimetr(self):
        return self.a + self.b + self.c + self.d

    def diags(self):
        return self.diag1, self.diag2


class Trapezoid(PlaneShapes):
    titele = "Трапеция"
    def __init__(self, a, b, c):  #
        super().__init__()
        self.a = a  # Нижнее основание
        self.b = b  # Верхнее основание
        self.c = c  # Стороны
        try:
            self.h = math.sqrt(self.c ** 2 - ((self.a - self.b)**2)/4)
        except ZeroDivisionError:
            "Err"
    def area(self):
        return ((self.a + self.b) * self.h) / 2


class Сube(VolumetricShapes):
    titele = "Куб"

    def __init__(self, x):
        super().__init__()
        self.x = x

    def volume(self):
        return self.x**3

    def area(self):
        return self.x**2 * 6


class Parallelepiped(VolumetricShapes):
    titele = "Параллелепипед"

    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        return self.a * self.b * self.c

    def area(self):
        return (self.a * self.b + self.a * self.c + self.c * self.b) * 2


class Sphere(Circle):
    titele = "Cфера"

    def __init__(self, r):
        super(Circle, self).__init__()
        self.r = r

    def volume(self):
        return 4 * math.pi * self.r**3 / 3

    def area(self):
        return 4 * self.r * math.pi


class Pyramid(VolumetricShapes):
    titele = "Пирамида (Тетраэдр)"

    def __init__(self, x):
        super(VolumetricShapes, self).__init__()
        self.x = x

    def height(self):
        return math.sqrt(2 * self.x / 3)

    def volume(self):
        return math.sqrt(2) * self.x**3 / 12

    def area(self):
        return math.sqrt(3) * self.x**2

class Сylinder(VolumetricShapes):
    titele = "Цилиндр"

    def __init__(self, r, h):
        super().__init__()
        self.r = r
        self.h = h

    def volume(self):
        return self.h * math.pi * self.r ** 2

    def area(self):
        return 2 * math.pi * self.r * self.h + 2 * math.pi * self.r ** 2

class Сone(VolumetricShapes):
    titele = "Конус"

    def __init__(self, l, r):
        super().__init__()
        self.r = r # Радиус
        self.l = l # Образующая
        self.h =  math.sqrt(l**2 - r**2)
        self.s = math.pi * self.r * (self.r + self.l)

    def volume(self):
        return (self.s * self.h)/3

    def area(self):
        return self.s

