class Point:
    def __init__(self, x = 0, y = 0):
        """ This is initializator

        Is called right after the Class instance was created.
        """
        print(f'Instance {self} is initialized.')
        self.x = x
        self.y = y

    def __del__(self):
        """ This is finalizator

        Is called right before garbage collector removes the Class instance.
        """
        print(f'Zero references are pointing to {self}. Cleaning up... ')

    def set_cords(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_cords(self) -> tuple:
        return self.x, self.y

pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt1.__dict__)
print(pt2.__dict__)
# print(pt1.get_cords())
# print(pt2.get_cords())
