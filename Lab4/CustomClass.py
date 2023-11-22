import math

class Vector2:
    customName = ""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"X: {self.x}  Y: {self.y}"

    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    @staticmethod
    def reverse(vector):
        return Vector2(-vector.x, -vector.y)

    @classmethod
    def from_values(cls, x, y):
        return Vector2(x, y)

obj1 = Vector2(3, 4)

print(obj1.length())
print(Vector2.reverse(Vector2(1, 1)))
print(Vector2.from_values(5, 6))