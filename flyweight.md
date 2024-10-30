# Flyweight Pattern in Python

The **Flyweight Pattern** is a structural design pattern used to minimize memory usage by sharing as much data as possible with similar objects. It’s especially effective when there are many instances of small, similar objects. The pattern involves storing shared, immutable data in a "flyweight" object and maintaining only essential, unique data outside of it.

Here’s an example of the Flyweight Pattern in Python, simulating a graphical application that renders many trees in a forest. The `Tree` class holds the shared intrinsic state (tree type and color), and a `TreeFactory` ensures that only one instance of each unique tree type is created.

### Example of the Flyweight Pattern in Python

```python
# Flyweight class to represent a tree
class Tree:
    def __init__(self, type_: str, color: str):
        self.type = type_
        self.color = color

    def display(self, x: int, y: int):
        return f"Tree of type '{self.type}' and color '{self.color}' located at ({x}, {y})"

# Flyweight Factory to manage shared instances of trees
class TreeFactory:
    _trees = {}

    @classmethod
    def get_tree(cls, type_: str, color: str):
        key = (type_, color)
        if key not in cls._trees:
            cls._trees[key] = Tree(type_, color)
        return cls._trees[key]

# Forest that uses the TreeFactory to create trees
class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x: int, y: int, type_: str, color: str):
        tree = TreeFactory.get_tree(type_, color)
        self.trees.append((tree, x, y))

    def display_trees(self):
        for tree, x, y in self.trees:
            print(tree.display(x, y))

# Usage
if __name__ == "__main__":
    forest = Forest()
    forest.plant_tree(1, 1, "Oak", "Green")
    forest.plant_tree(2, 3, "Pine", "Dark Green")
    forest.plant_tree(1, 2, "Oak", "Green")  # Reuses the "Oak" "Green" instance
    forest.plant_tree(3, 1, "Pine", "Dark Green")  # Reuses the "Pine" "Dark Green" instance
    forest.display_trees()
```

### Explanation

1. **Tree (Flyweight)**: Represents the shared intrinsic state (e.g., type and color) of trees.
  
2. **TreeFactory (Flyweight Factory)**: Manages instances of `Tree` objects. When `get_tree()` is called, it either creates a new `Tree` instance (if that type and color combo doesn’t exist) or returns an existing one.

3. **Forest**: This class represents a forest that can plant trees by calling the `TreeFactory` and holds references to each `Tree`’s location.

### Output

Running this code will display:

```
Tree of type 'Oak' and color 'Green' located at (1, 1)
Tree of type 'Pine' and color 'Dark Green' located at (2, 3)
Tree of type 'Oak' and color 'Green' located at (1, 2)
Tree of type 'Pine' and color 'Dark Green' located at (3, 1)
```

### Benefits of the Flyweight Pattern

- **Memory Efficiency**: Reduces the number of instances by reusing shared, intrinsic data.
- **Performance**: Can significantly reduce memory usage in applications with many similar objects.

### Try it yourself

Here’s the working implementation of the Flyweight Pattern in [Python](src/flyweight.py)
