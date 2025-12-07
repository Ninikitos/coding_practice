# super() — is a way to call a parent method without naming the parent explicitly.
# It finds the next class in the inheritance chain and calls its method (MRO).

# MRO (Method Resolution Order)
# When a method is called, Python must decide which class to take it from.
# If there are multiple parents, it looks in a specific order (MRO).

# class A: pass
# class B(A): pass
# class E(A): pass
# class C(A): pass
# class D(B, C): pass
#
# print(D.__mro__)
# The search order will be: (D, B, C, A, object)
# Python goes from left to right, like a tree traversal.
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
#  <class '__main__.A'>, <class 'object'>)

# Why not D, B, A, C, A, object?
# Python merges common parents to avoid calling them multiple times.

# It preserves the inheritance order (B before C);
# Respects parent hierarchy (if B inherits from A, then A goes after B);
# Common ancestors (A, object) are not duplicated. That’s why it is not
# D, B, A, C, A, object.

# How MRO is built
# Start with D.
# Look at its parents B and C — add them to the list after D (MRO list).
# Then take parents of B and C: both point to A.
# Python adds A only once, right before object.
# Python goes through all classes “left to right” like a tree.

# How to call super()?
# 1. super().method()

# Bound super — bound to an instance
# Python knows which self to use.
# super(B, self).method() || super().method()
# both variants are bound to the object (self).

# Unbound super — not bound to an instance
# super(B)

# Calling inside __init__()

# Errors
# TypeError: super(type, obj): obj must be an instance or subtype of type
# Wrong second argument: super(B, A()) — A is not an instance of B

# super(B) without an object
# Unbound super cannot call instance methods

# super() does not work in static methods
# No self → no context to determine the class

# Iterate over all classes in an MRO list
# for cls in D.__mro__:
#     print(cls.__name__)

class S:
    def print_new(self):
        print('S')
class A(S):
    def print_new(self):
        print('A')
class B(A):
    def print_new(self):
        print('Print from B')
class E(A): pass
class C(A):
    def print_new(self):
        print('Print from C')

    def super_print(self):
        print('Super print')
class D(B, C):
    def __init__(self):
        super().__init__()
        # super().print_new()
    def test(self):
        print('From D')

d = D()
print(D.__mro__)
d.super_print()