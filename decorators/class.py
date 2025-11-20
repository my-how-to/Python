#=========================================
#   DECORATORS — CLASS DECORATORS
#=========================================
#
# This file explains how decorators can be applied to ENTIRE classes.
#
# Class decorators are functions that receive a class, modify it, and
# return the modified class. They are useful for:
#
#    - adding methods or attributes to classes
#    - enforcing rules (validation)
#    - registering classes automatically
#    - modifying or wrapping class behavior
#    - building plugin systems
#
#All examples are runnable and include explanations.

import functools

# ============================================================
# 1. BASIC CLASS DECORATOR
# ============================================================

"""
A class decorator is just a function that takes a CLASS and returns a CLASS.
"""

def add_repr(cls):
    """
    Add a __repr__ method to any class that does not define one.
    """
    if not hasattr(cls, "__repr__"):
        def __repr__(self):
            return f"<{cls.__name__} {self.__dict__}>"
        cls.__repr__ = __repr__
    return cls

@add_repr
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# ============================================================
# 2. CLASS DECORATOR THAT MODIFIES INIT
# ============================================================

"""
We can intercept and enhance __init__.
This decorator logs the creation of objects.
"""

def log_init(cls):
    original_init = cls.__init__

    @functools.wraps(original_init)
    def new_init(self, *args, **kwargs):
        print(f"[INIT] Creating instance of {cls.__name__}")
        original_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls

@log_init
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# ============================================================
# 3. CLASS DECORATOR FOR VALIDATION
# ============================================================

"""
Automatically validate attributes after creation.
Useful for data models.
"""

def validate_non_empty(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        for key, value in self.__dict__.items():
            if value == "" or value is None:
                raise ValueError(f"Attribute '{key}' cannot be empty")
    cls.__init__ = new_init
    return cls

@validate_non_empty
class Account:
    def __init__(self, username, email):
        self.username = username
        self.email = email


# ============================================================
# 4. CLASS DECORATOR THAT REGISTERS CLASSES
# ============================================================

"""
Used in plugin systems, factories, or frameworks.
Each decorated class is stored automatically.
"""

REGISTRY = {}

def register(cls):
    REGISTRY[cls.__name__] = cls
    return cls

@register
class Car:
    pass

@register
class Plane:
    pass


# ============================================================
# 5. CLASS DECORATOR USING PARAMETERS
# ============================================================

"""
To accept parameters, we wrap the decorator inside another function.
"""

def tag(label):
    def decorator(cls):
        cls.tag = label
        return cls
    return decorator

@tag("database-model")
class Record:
    pass


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    # 1. Basic __repr__ decorator
    u = User("Alex", 36)
    print(u)

    # 2. Modified __init__
    p = Product("Chair", 49.9)

    # 3. Validation example
    try:
        bad = Account("", "test@example.com")
    except ValueError as e:
        print("[VALIDATION ERROR]", e)

    # 4. Registry
    print("Registered classes:", REGISTRY)

    # 5. Class decorator with arguments
    model = Record()
    print("Record tag:", Record.tag)
