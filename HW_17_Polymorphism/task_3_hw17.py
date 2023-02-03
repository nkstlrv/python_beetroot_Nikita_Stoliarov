class Fraction:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        a = self.x + other.x
        b = self.y + other.y
        return a, b

    def __sub__(self, other):
        a = self.x - other.x
        b = self.y - other.y
        return a, b

    def __mul__(self, other):
        a = self.x * other.x
        b = self.y * other.y
        return a, b

    def __truediv__(self, other):
        try:
            a = self.x / other.x
            b = self.y / other.y
        except ZeroDivisionError:
            return "You can't divide by zero"
        return a, b


if __name__ == "__main__":

    x = Fraction(4, 2)
    y = Fraction(3, 0)

    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
