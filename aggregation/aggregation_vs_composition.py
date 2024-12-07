"""
Aggregation vs Composition :

Relationship :
    Aggregation : "Has-a" (weaker relationship)
    Composition : "Part-of" (stronger relationship)

Object Lifespan :
	Aggregation : Contained objects can exist independently
	Composition : Contained objects depend on the parent for existence

Dependency :
	Aggregation : Contained objects are loosely coupled
	Composition : Contained objects are tightly coupled

Example :
	Aggregation : Library has Books (Books can exist without Library)
	Composition : Engine is "part of" a Car (Engine cannot exist without Car)
"""

