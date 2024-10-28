
# Abstract Factory Pattern in Python

The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. It’s particularly useful when you want to create multiple objects in a coordinated way and hide the details of how they are instantiated.
 
```python
from abc import ABC, abstractmethod

# Abstract products
class Button(ABC):
    @abstractmethod
    def click(self) -> str:
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self) -> str:
        pass

# Concrete products for Windows
class WindowsButton(Button):
    def click(self) -> str:
        return "Windows Button Clicked!"

class WindowsCheckbox(Checkbox):
    def check(self) -> str:
        return "Windows Checkbox Checked!"

# Concrete products for macOS
class MacButton(Button):
    def click(self) -> str:
        return "Mac Button Clicked!"

class MacCheckbox(Checkbox):
    def check(self) -> str:
        return "Mac Checkbox Checked!"

# Abstract factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete factories for Windows and macOS
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Client code
def create_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.click())
    print(checkbox.check())

# Usage
if __name__ == "__main__":
    os_type = "Windows"  # Imagine this is detected dynamically
    factory = WindowsFactory() if os_type == "Windows" else MacFactory()
    create_ui(factory)
```

---

## Explanation

- **Abstract Products**: The `Button` and `Checkbox` classes define the interfaces for the products in our GUI (buttons and checkboxes).
  
- **Concrete Products**: 
  - `WindowsButton` and `WindowsCheckbox` implement the `Button` and `Checkbox` interfaces for Windows.
  - `MacButton` and `MacCheckbox` implement the `Button` and `Checkbox` interfaces for macOS.

- **Abstract Factory**: The `GUIFactory` interface declares methods to create the abstract products (`create_button` and `create_checkbox`).

- **Concrete Factories**: 
  - `WindowsFactory` implements `GUIFactory` to produce Windows-style buttons and checkboxes.
  - `MacFactory` implements `GUIFactory` to produce macOS-style buttons and checkboxes.

- **Client Code**: `create_ui` takes a factory as input and uses it to create a button and a checkbox without knowing the specific types.

---

## Output

If `os_type` is set to `"Windows"`, the output will be:

```
Windows Button Clicked!
Windows Checkbox Checked!
```

If `os_type` is set to something else (like `"MacOS"`), the output will be:

```
Mac Button Clicked!
Mac Checkbox Checked!
```

This pattern lets you add new OS themes by simply creating additional factories and product implementations following the same interfaces.

### Try it yourself

Here’s the working implementation of the Abstract Factory Pattern in [Python](src/abstract_factory.py)
