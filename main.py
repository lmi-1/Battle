class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"
a = Dot(1, 1)
b = Dot(2, 1)
c = Dot(1, 1)
print( a == c)
print(a, b, c)
