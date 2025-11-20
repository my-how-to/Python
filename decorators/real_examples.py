"""
=========================================
   DECORATORS — REAL-WORLD EXAMPLES
=========================================

This file contains practical decorators used in real projects:
    - logging
    - timing performance
    - caching results
    - retrying failed operations
    - validation and permission examples

All examples are runnable and include clear explanations.
"""

import time
import functools

# ============================================================
# 1. LOGGING DECORATOR
# ============================================================

"""
A logging decorator is often used in automation, debugging, or APIs.
It prints (or stores) information about function calls.
"""

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b


# ============================================================
# 2. TIMER DECORATOR
# ============================================================

"""
Measures how long a function takes to run.
Useful in optimization, analytics, and heavy computations.
"""

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_operation():
    time.sleep(0.5)
    return "done"


# ============================================================
# 3. SIMPLE CACHE DECORATOR
# ============================================================

"""
Caches function results.
If the same arguments are used again, the function is not re-run.

This is useful for expensive computations.
"""

def simple_cache(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"[CACHE] Returning cached result for {args}")
            return cache[args]
        print(f"[CACHE] Computing result for {args}")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@simple_cache
def multiply(a, b):
    time.sleep(0.3)
    return a * b


# ============================================================
# 4. RETRY DECORATOR (WITH ARGUMENTS)
# ============================================================

"""
Retries a function multiple times if it raises an exception.
Used in network calls, file operations, unstable systems.
"""

def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[RETRY] Attempt {attempt}/{times} failed: {e}")
                    if attempt == times:
                        raise
        return wrapper
    return decorator

count = 0

@retry(times=3)
def unstable():
    global count
    count += 1
    if count < 3:
        raise ValueError("Still failing...")
    return "Success on third attempt!"


# ============================================================
# 5. VALIDATION DECORATOR
# ============================================================

"""
Validates arguments before calling a function.
Used in forms, APIs, CLI tools.
"""

def require_positive(func):
    @functools.wraps(func)
    def wrapper(x):
        if x <= 0:
            raise ValueError("Value must be positive")
        return func(x)
    return wrapper

@require_positive
def square(x):
    return x * x


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    print(add(2, 3))
    print(slow_operation())
    print(multiply(3, 4))
    print(multiply(3, 4))  # cached
    print(unstable())
    print(square(5))
