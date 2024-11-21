import math

class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = [0, 0, 0]
        self.filled = True


    def get_color(self):
        return self.__color

    def is_valid_color(self, r, g, b):
        if not (isinstance(r, int) is isinstance(g, int) is isinstance(b, int)):
            return False
        elif 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return False

    def set_color(self, r, g, b):
        if self.is_valid_color(r, g, b):
            self.__color = [r, g, b]


    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not (isinstance(side, int) and side > 0):
                return False
            return True

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self._Figure__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)
        self.radius = radius

    def get_square(self):
        return math.pi * self.radius ** 2

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.radius = new_sides[0]
            super().set_sides(*new_sides)


class Triangle(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 3
        super().__init__(color, *sides)
        self.__sides = [1, 1, 1] if len(sides) != self.sides_count else list(sides)

    def get_square(self):
        a, b, c = self.__sides
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color, side_length)
        if isinstance(side_length, int) and side_length > 0:
            self.set_sides(*([side_length] * self.sides_count))
        else:
            self.set_sides(*([1] * self.sides_count))

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


