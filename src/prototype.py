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
