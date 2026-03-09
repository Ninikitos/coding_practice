class Point:
    MIN_COORD = 10
    MAX_COORD = 20

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_coords(self, x: int, y: int):
        if self.MIN_COORD < x < self.MAX_COORD:
            self.x = x
            self.y = y
    # This will create a new instance attribute.
    # def set_bound(self, left: int):
    #     self.MIN_COORD = left

    @classmethod
    def set_bound(cls, left: int):
        cls.MIN_COORD = left

p = Point(1, 2)
p1 = Point(10, 20)
p1.set_bound(15)
# def set_bound - not a class method. self -> to instance of a Class
# {'x': 10, 'y': 20, 'MIN_COORD': 15}

# def set_bound - as a classmethod. cls -> Class
# {'x': 10, 'y': 20}
print(p1.__dict__)
# 'MIN_COORD': 10, 'MAX_COORD': 20,
print(Point.__dict__)


# ------------------------
# Point.__setattr__(self, key, value) - atr. changes
# Point.__getattribute__(self, item) - atr. item is passed and it is exists
# Point.__getattr__(self, item) - atr. does not exist
# Point.__delattr__(self, item) - atr. deletion no matter if it exists