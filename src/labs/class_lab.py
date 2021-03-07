class Rectangle:
    def __init__(self, width):
        self.width = width

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        if value <= 0:
            raise ValueError(f"Invalid value has passed. {value}")

        self._width = value

    def __str__(self):
        return f'Rectangle of width={self.width}'

rec = Rectangle(5)
print(rec)

try:
    rec = Rectangle(0)
except ValueError as e:
    print(f"Value error has just happened. {e}")
except:
    print("Generic exception")
finally:
    print("finally does work!")
