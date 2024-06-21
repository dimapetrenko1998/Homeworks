class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __is_valid_sides(self, *new_sides):
        return all(side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)
        self.__radius = sides[0]

    def get_square(self):
        return 3.14 * self.__radius ** 2  # Площадь круга


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)
        self.__height = 3 ** 0.5 / 2 * sides[0]

    def get_square(self):
        # Рассчет площади треугольника
        p = sum(self._Figure__sides) / 2
        return (p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)

    def get_volume(self):
        return self._Figure__sides[0] ** 3  # Объем куба


circle1 = Circle((200, 200, 100), (10, 15, 6), True)
cube1 = Cube((222, 35, 130), (6, 6, 6), False)
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
circle1.set_sides(15)
print(cube1._Figure__sides)
print(circle1._Figure__sides)
print(len(circle1))
print(cube1.get_volume())
