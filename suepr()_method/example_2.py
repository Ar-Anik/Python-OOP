class BaseWidget:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Displaying {self.name}")


class CustomWidget(BaseWidget):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def display(self):
        print(f"Custom display for {self.name} in color {self.color}")
        super(CustomWidget, self).display()


class AdvancedCustomWidget(CustomWidget):
    def __init__(self, name, color, size):
        super().__init__(name, color)
        self.size = size

    def display(self):
        print(f"Advanced custom display for {self.name} in color {self.color} and size {self.size}")
        super(AdvancedCustomWidget, self).display()


advanced_widget = AdvancedCustomWidget("Button", "Blue", "Large")
advanced_widget.display()
