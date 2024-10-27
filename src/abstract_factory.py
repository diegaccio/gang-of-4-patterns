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