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