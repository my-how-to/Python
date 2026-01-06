# PYTHON EXCEPTIONS — QUICK REFERENCE & CHEATSHEET

[BACK](../README.md)

Author: Alexandru Petrenco (with AI assistance from GPT-5)

This file is a certification-oriented summary of the most common
Python exceptions, when they occur, and examples that trigger them.

Useful for:
- PCEP exam
- PCAP exam
- Interview prep
- Daily coding reference

---

# CERTIFICATION TIP

For PCEP and PCAP, the most commonly tested exceptions are:

- **ValueError**
- **TypeError**
- **IndexError**
- **KeyError**
- **ZeroDivisionError**
- **FileNotFoundError**
- **NameError**

Master these and you'll cover **90%** of real-world and exam cases.

---

# Input and Type Errors

| Exception     | When It Happens                                   | Example                     |
|---------------|----------------------------------------------------|-----------------------------|
| **ValueError** | Correct type but invalid value                     | `int("abc")`               |
| **TypeError**  | Using wrong type for an operation                  | `"5" + 3`                  |
| **NameError**  | Using a variable that is not defined               | `print(x)`                 |
| **IndexError** | Accessing a list/tuple index that doesn't exist    | `[1,2,3][5]`               |
| **KeyError**   | Dictionary key does not exist                      | `my_dict["missing"]`       |

---

# Math and Numeric Errors

| Exception            | When It Happens                            | Example               |
|----------------------|---------------------------------------------|------------------------|
| **ZeroDivisionError** | Dividing by zero                            | `5 / 0`               |
| **OverflowError**     | Number too large for memory (rare)          | `math.exp(1000)`      |
| **FloatingPointError**| Floating point calculation problem (rare)   | Advanced math issues  |

---

# File and I/O Errors

| Exception           | When It Happens                                  | Example                      |
|---------------------|---------------------------------------------------|------------------------------|
| **FileNotFoundError** | File does not exist                               | `open("missing.txt")`       |
| **PermissionError**   | No permission to read/write file                  | Writing to read-only file    |
| **IOError**           | Generic I/O issue (Python 2 style, now OSError)   | Input/output failures        |

---

# Import and Module Errors

| Exception              | When It Happens                    | Example                              |
|------------------------|-------------------------------------|----------------------------------------|
| **ImportError**         | Module exists but import fails       | `from math import unknown_func`        |
| **ModuleNotFoundError** | Module does not exist                | `import not_existing_module`           |

---

# Logic and Syntax Errors

| Exception          | When It Happens                        | Example                     |
|--------------------|-----------------------------------------|-----------------------------|
| **AssertionError**   | `assert` condition is false            | `assert 2 > 3`             |
| **SyntaxError**      | Python syntax is invalid               | `if True print("hi")`      |
| **IndentationError** | Wrong indentation                      | Misaligned code blocks      |

---

# Other Useful Exceptions

| Exception          | When It Happens                                | Example           |
|--------------------|-------------------------------------------------|-------------------|
| **AttributeError**   | Missing object attribute/method                 | `"abc".push()`    |
| **RuntimeError**     | Generic runtime failure                         | Recursion issues  |
| **RecursionError**   | Max recursion depth exceeded                    | Infinite recursion |
| **StopIteration**    | Iterator has no more items (internal to `for`) | Manual iteration   |

---

# Final Notes

- Python exceptions form a full inheritance tree under `BaseException`.
- Most exceptions come from logical errors, not Python itself.
- In certification exams, **understanding WHEN exceptions happen** is more important than memorizing names.

---

[BACK](../README.md)