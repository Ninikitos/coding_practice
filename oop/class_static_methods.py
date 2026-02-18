# @classmethod and @staticmethod
# Both are decorators of methods that are defined in class.

# @classmethod helps class method to call class attributes(cls) but
# cannot call instance attributes(self).
# - Now we can call this method from a class without instance init Vector.validate(5).
# - cls will be passed into validate function automatically by python interpreter
# - self used in __init__ for two reasons:
#    - self has information of a class that
# @staticmethod doesn't have access to class or class instance attributes.
# This is handy if a method is related to the class logically or semantically.
# Also it could be treated as a helper function.

# self — access to class and instance attributes;
# cls — access to class attributes;
# staticmethod — helper/services method.

class Vector:
    # Class attributes
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg: int):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x: int, y: int):
        # instance attributes
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def norn2(x: int, y: int) -> int:
        return x*2 + y*2

print(Vector.validate(3))