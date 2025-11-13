# 🧩 Patterns Overview

This document lists all **23 classic Design Patterns** as described by the *Gang of Four (GoF)*, grouped by category.  
Each entry includes a short, one-line description and a link to the corresponding example file.

---

## 🏗️ Creational Patterns

| Pattern | Description |
|----------|-------------|
| [**Factory Method**](factory.py) | Creates objects without specifying the exact class to instantiate. |
| [**Abstract Factory**](abstract_factory.py) | Produces families of related objects without specifying their concrete classes. |
| [**Builder**](builder.py) | Separates the construction of a complex object from its representation. |
| [**Prototype**](prototype.py) | Creates new objects by copying existing ones (cloning). |
| [**Singleton**](singleton.py) | Ensures a class has only one instance and provides a global access point. |

---

## 🧱 Structural Patterns

| Pattern | Description |
|----------|-------------|
| [**Adapter**](adapter.py) | Bridges incompatible interfaces so that classes can work together. |
| [**Bridge**](bridge.py) | Separates an object’s abstraction from its implementation so they can vary independently. |
| [**Composite**](composite.py) | Composes objects into tree structures to represent part-whole hierarchies. |
| [**Decorator**](decorator.py) | Dynamically adds or modifies functionality of an object at runtime. |
| [**Facade**](facade.py) | Provides a simplified interface to a larger body of code. |
| [**Flyweight**](flyweight.py) | Reduces memory usage by sharing common data between similar objects. |
| [**Proxy**](proxy.py) | Controls access to another object, often adding additional behavior. |

---

## 🔁 Behavioral Patterns

| Pattern | Description |
|----------|-------------|
| [**Chain of Responsibility**](chain_of_responsibility.py) | Passes requests along a chain of handlers until one processes it. |
| [**Command**](command.py) | Encapsulates a request as an object, allowing parameterization and queuing of operations. |
| [**Interpreter**](interpreter.py) | Defines a grammar and interpreter for a language or symbolic expressions. |
| [**Iterator**](iterator.py) | Provides a way to access elements of a collection without exposing its structure. |
| [**Mediator**](mediator.py) | Defines an object that coordinates communication between multiple objects. |
| [**Memento**](memento.py) | Captures and restores an object’s internal state without exposing details. |
| [**Observer**](observer.py) | Allows objects to subscribe and react to events or state changes in another object. |
| [**State**](state.py) | Allows an object to alter its behavior when its internal state changes. |
| [**Strategy**](strategy.py) | Defines a family of algorithms and makes them interchangeable at runtime. |
| [**Template Method**](template_method.py) | Defines the skeleton of an algorithm, letting subclasses override certain steps. |
| [**Visitor**](visitor.py) | Separates an algorithm from the objects it operates on for easier extension. |

---

## 📚 Notes

Each pattern includes:
- A **Before Version** showing the old manual or repetitive approach.
- A **Pattern Version** showing the improved structured solution.
- Consistent **comments**, **example output**, and a short **history** in each file.

> This overview serves as a reference and progress checklist as the repository expands to include all 23 patterns.
