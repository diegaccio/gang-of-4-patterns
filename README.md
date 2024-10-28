# Gang of Four (GoF) Design Patterns

The Gang of Four (GoF) design patterns are divided into three main categories: **Creational**, **Structural**, and **Behavioral**.

## 1. Creational Patterns
These patterns deal with object creation mechanisms.

- **[Abstract Factory](abstract_factory.md)**: Creates families of related objects without specifying their concrete classes.
- **[Builder](builder.md)**: Constructs complex objects step-by-step, allowing for different representations.
- **[Factory Method](factory_method.md)**: Defines an interface for creating an object, letting subclasses decide which class to instantiate.
- **[Prototype](prototype.md)**: Creates new objects by copying an existing object, known as a prototype.
- **Singleton**: Ensures that a class has only one instance and provides a global point of access to it.

## 2. Structural Patterns
These patterns deal with object composition, simplifying the relationships between objects.

- **Adapter**: Converts the interface of a class into another interface that clients expect.
- **Bridge**: Decouples an abstraction from its implementation, allowing both to vary independently.
- **Composite**: Composes objects into tree-like structures to represent part-whole hierarchies.
- **[Decorator](decorator.md)**: Adds responsibilities to objects dynamically without modifying their class.
- **Facade**: Provides a unified interface to a set of interfaces in a subsystem.
- **Flyweight**: Uses sharing to support large numbers of fine-grained objects efficiently.
- **Proxy**: Provides a surrogate or placeholder for another object to control access to it.

## 3. Behavioral Patterns
These patterns deal with object interaction and communication.

- **Chain of Responsibility**: Passes a request along a chain of handlers, where each handler decides to process it or pass it along.
- **Command**: Encapsulates a request as an object, allowing for parameterization and queuing of requests.
- **Interpreter**: Defines a representation for a language's grammar and uses it to interpret sentences in the language.
- **Iterator**: Provides a way to access elements of a collection sequentially without exposing the underlying representation.
- **Mediator**: Defines an object that centralizes and controls communication between objects.
- **Memento**: Allows capturing and restoring an object’s internal state without violating encapsulation.
- **Observer**: Defines a dependency between objects so that when one changes state, all its dependents are notified.
- **State**: Allows an object to alter its behavior when its internal state changes.
- **Strategy**: Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
- **Template Method**: Defines the skeleton of an algorithm, with steps deferred to subclasses.
- **Visitor**: Allows adding further operations to objects without modifying their classes.

*These patterns were introduced in* **Design Patterns: Elements of Reusable Object-Oriented Software** *by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides.*
