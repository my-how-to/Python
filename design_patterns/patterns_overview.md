# Patterns Overview

This document lists all **23 classic Design Patterns** as described by the *Gang of Four (GoF)*, grouped by category.
Each entry includes a short, one-line description and a link to the corresponding example file.

> ⚠️ **Note:**
> Patterns are named using simple filenames like `strategy.py`, `observer.py`, etc.
> Only implemented patterns link to real files. Others link to `missing_pattern.md`.

---

## Creational Patterns

| Pattern                                       | Description                                                                     |
| --------------------------------------------- | ------------------------------------------------------------------------------- |
| [**factory.py**](factory.py)                  | Creates objects without specifying the exact class to instantiate.              |
| [**abstract_factory.py**](abstract_factory.py) | Produces families of related objects without specifying their concrete classes. |
| [**builder.py**](builder.md)          | Separates the construction of a complex object from its representation.         |
| [**prototype.py**](prototype.py)              | Creates new objects by copying existing ones (cloning).                         |
| [**singleton.py**](singleton.py)              | Ensures a class has only one instance and provides a global access point.       |

---

## Structural Patterns

| Pattern                                | Description                                                                               |
| -------------------------------------- | ----------------------------------------------------------------------------------------- |
| [**adapter.py**](adapter.py)           | Bridges incompatible interfaces so that classes can work together.                        |
| [**bridge.py**](missing_pattern.md)    | Separates an object’s abstraction from its implementation so they can vary independently. |
| [**composite.py**](missing_pattern.md) | Composes objects into tree structures to represent part-whole hierarchies.                |
| [**decorator.py**](decorator.py)       | Dynamically adds or modifies functionality of an object at runtime.                       |
| [**facade.py**](missing_pattern.md)    | Provides a simplified interface to a larger body of code.                                 |
| [**flyweight.py**](missing_pattern.md) | Reduces memory usage by sharing common data between similar objects.                      |
| [**proxy.py**](missing_pattern.md)     | Controls access to another object, often adding additional behavior.                      |

---

## Behavioral Patterns

| Pattern                                              | Description                                                                               |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| [**chain_of_responsibility.py**](missing_pattern.md) | Passes requests along a chain of handlers until one processes it.                         |
| [**command.py**](missing_pattern.md)                 | Encapsulates a request as an object, allowing parameterization and queuing of operations. |
| [**interpreter.py**](missing_pattern.md)             | Defines a grammar and interpreter for a language or symbolic expressions.                 |
| [**iterator.py**](missing_pattern.md)                | Provides a way to access elements of a collection without exposing its structure.         |
| [**mediator.py**](missing_pattern.md)                | Defines an object that coordinates communication between multiple objects.                |
| [**memento.py**](missing_pattern.md)                 | Captures and restores an object’s internal state without exposing details.                |
| [**observer.py**](observer.py)                       | Allows objects to subscribe and react to events or state changes in another object.       |
| [**state.py**](missing_pattern.md)                   | Allows an object to alter its behavior when its internal state changes.                   |
| [**strategy.py**](missing_pattern.md)                | Defines a family of algorithms and makes them interchangeable at runtime.                 |
| [**template_method.py**](missing_pattern.md)         | Defines the skeleton of an algorithm, letting subclasses override certain steps.          |
| [**visitor.py**](missing_pattern.md)                 | Separates an algorithm from the objects it operates on for easier extension.              |

---

## Notes

Each pattern includes:

* A **Before Version** showing the old manual or repetitive approach.
* A **Pattern Version** showing the improved structured solution.
* Consistent **comments**, **example output**, and a short **history** in each file.

> This overview serves as a reference and progress checklist as the repository expands to include all 23 patterns.
