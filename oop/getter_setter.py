class Point:
    """
    A class that stores x, y coordinates for a point.

    The coordinates are stored as 'private' attributes (_x, _y) — the underscore
    is just a convention to signal "don't touch these directly", but Python won't
    actually stop you. You're supposed to use the getter/setter methods instead.

    Practical example:
        p = Point(1, 2)        # create a point at (1, 2)
        p.set_coords(5, 10)    # update the coordinates
        print(p.get_coords())  # → (5, 10)

    Heads up:
        Doing p.coords = 20 and p.coords won't touch _x or _y at all.
        Python will just create a brand new attribute called 'coords' on the fly
        and store 20 there — it won't raise an error, it just silently does
        something you probably didn't intend.

        p = Point(1, 2)
        p.coords = 20       # creates a NEW attribute, doesn't change _x or _y
        foo = p.coords      # reads that new attribute
        print(foo)          # → 20  (not the actual coordinates!)

        This is why properties (@property) exist to let you control what
        happens when someone does p.coords = 20. That's the next level up from this.
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # Getters and Setters example
    # def set_coords(self, x, y):
    #     self._x = x
    #     self._y = y
    #
    # def get_coords(self):
    #     return self._x, self._y

    @property
    def x(self):
        return self._x # called when you READ p.x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('x must be a number')
        self._x = value # called when you WRITE p.x = 30

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('y must be a number')
        self._y = value


p = Point(1, 2)
print(p.x)      # → 1       (triggers the getter)
p.x = 10        # → ok      (triggers the setter, validates the value)
p.x = "hello"   # → TypeError: x must be a number
p._x = 1  # → still works, underscore is just a convention!