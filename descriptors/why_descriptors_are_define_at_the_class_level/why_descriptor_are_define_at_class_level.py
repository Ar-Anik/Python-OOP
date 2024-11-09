"""
Descriptors in Python are objects with specific methods—such as __get__, __set__, and __delete__—that control how attribute access works.
When we set a descriptor as a class-level attribute, these special methods allow the descriptor to manage access to the attribute across
all instances of the class.

Here’s why descriptors are defined at the class level and not at the instance level:

1. Consistency Across Instances : Let’s say we create a descriptor to manage how a particular attribute is accessed. By defining this descriptor
at the class level, we ensure that every instance of the class accesses this attribute in the same way, following the descriptor’s rules. If we
put the descriptor at the instance level, it would only apply to that particular instance, which would defeat the purpose of having a descriptor
control attribute access in a uniform way. By defining it at the class level, all instances use the same descriptor logic.

2. Triggering the Descriptor Protocol : The descriptor protocol is a set of rules in Python that gets activated only when a descriptor is assigned
as a class attribute. Means the descriptor protocol is effective only if it’s triggered through attribute lookup chain. When a descriptor is defined
on the class, it can be reached during attribute lookup for all instances. If it were assigned at the instance level, it wouldn’t participate in this
lookup chain, and its special methods wouldn’t be triggered automatically.

On the other hand :
---> When we assign a descriptor to an instance, it gets stored directly in that instance’s __dict__ as a regular attribute. Python accesses it directly as
a regular object stored in the dictionary. Since it is no longer located in the class, the descriptor's special methods (like __get__ or __set__) are not
involved in attribute access, and the descriptor is treated as a typical instance attribute.
"""
