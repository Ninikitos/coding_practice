class Point(object):
    """
    A Singleton class that ensures only ONE instance of Point ever exists.
    No matter how many times you call Point(), you always get back the exact same object.

    How it works:
        __new__ is the method Python calls BEFORE __init__ when creating an object.
        Normally you don't touch it, but here we intercept it to check if an
        instance already exists before allowing a new one to be created.

        first call  - instance is None - create it, store it, return it
        second call - instance exists  - skip creation, return the same one

    __new__ vs __init__:
        __new__   - creates the object
        __init__  - initializes the object

        p = Point()
        # Python calls __new__ first  - are we allowed to create this?
        # Python calls __init__ second - ok set it up

    Real world use cases:
        - database connection  - you only ever want ONE connection open
        - config manager       - one source of truth for app settings
        - logger               - one logger writing to one file
    """
    instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

p = Point()
p2 = Point()
print(id(p) == id(p2))
print(p is p2)