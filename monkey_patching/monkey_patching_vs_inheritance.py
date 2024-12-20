"""
1. Concept
# Definition
Monkey Patching: Modifying or extending an existing class or module at runtime.
Inheritance: Creating a new class that derives from an existing class to extend or override behavior.

# Purpose
Monkey Patching: To quickly add, override, or modify behavior without modifying the original source code.
Inheritance: To reuse and extend functionality in a structured and hierarchical manner.


2. Implementation
# How It Works
Monkey Patching: Assigns new attributes or methods directly to an existing class or instance at runtime.
Inheritance: Creates a new class by inheriting from a parent class, adding or overriding its methods.


3. Use Cases
# When to Use
Monkey Patching:
    1. Temporary fixes or quick modifications.
    2. Altering third-party library behavior.
Inheritance:
    1. Adding structured and reusable functionality.
    2. Overriding or extending existing class behavior in a maintainable way.

# Real-Life Examples
Monkey Patching: Fixing bugs in libraries without changing their source code.
Inheritance: Creating specialized classes like AdminUser from a User class.


4. Advantages
# Flexibility
Monkey Patching: Can modify behavior dynamically at runtime.
Inheritance: Provides a clean and structured way to extend functionality.

# Speed
Monkey Patching: Useful for quick, temporary fixes.
Inheritance: Changes apply only to the subclass and its instances.


5. Drawbacks
# Maintainability
Monkey Patching: Can lead to difficult-to-debug code due to runtime modifications.
Inheritance: Can lead to overly complex hierarchies if overused.

# Predictability
Monkey Patching: Behavior may become unpredictable if multiple patches are applied.
Inheritance: Behavior remains predictable and consistent.

# Scope
Monkey Patching: Changes apply globally to all instances of the class.
Inheritance: Changes apply only to the subclass and its instances.


6. Alternatives
Monkey Patching: Use composition, mixins, or decorators for modifications.
Inheritance: Use composition or delegation instead of deep inheritance hierarchies.

"""