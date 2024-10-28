
# Prototype Pattern

The Prototype Pattern is a creational design pattern that allows you to create new objects by copying existing instances, known as prototypes. This pattern is useful when creating new instances is resource-intensive, or when you want to avoid complex initialization processes.

## Example of the Prototype Pattern in Python

In this example, we’ll create a Book prototype and clone it to make new copies. We'll also see how to modify copies without affecting the original prototype.
 
```python
import copy

# The Prototype base class
class Prototype:
    def clone(self):
        # Return a deep copy of the instance
        return copy.deepcopy(self)

# Concrete Prototype class
class Book(Prototype):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.tags = []

    def __str__(self):
        return f"Book(title={self.title}, author={self.author}, price={self.price}, tags={self.tags})"

    def add_tag(self, tag):
        self.tags.append(tag)

# Usage
if __name__ == "__main__":
    # Create an original book
    original_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
    original_book.add_tag("classic")
    
    # Clone the original book
    cloned_book = original_book.clone()
    cloned_book.title = "The Great Gatsby (Clone)"
    cloned_book.add_tag("duplicate")

    # Displaying both books
    print("Original Book:", original_book)
    print("Cloned Book:", cloned_book)

```

---

## Explanation

- **Prototype Class**: The `Prototype` class provides a `clone` method that uses `copy.deepcopy` to create a new, independent copy of an object. This way, changes to the cloned object don’t affect the original.

- **Concrete Prototype  (`Book`)**: The `Book` class extends `Prototype` and includes additional attributes like title, author, and price. We also add a method to append tags.
  
- **Cloning in Action**: We create an instance of `Book`, add a `tag`, then clone it. The cloned book can have its own title and tags without altering the original book. 

---

## Output

When you run this code, the output will be:

```
Original Book: Book(title=The Great Gatsby, author=F. Scott Fitzgerald, price=10.99, tags=['classic'])
Cloned Book: Book(title=The Great Gatsby (Clone), author=F. Scott Fitzgerald, price=10.99, tags=['classic', 'duplicate'])
```

With the Prototype Pattern, you can create independent copies of objects and customize them without impacting the original instance. This is especially useful when working with objects that have complex or nested data.

### Try it yourself

Here’s the working implementation of the Prototype Pattern in [Python](src/prototype.py)