class Room:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Room({self.name})"

class House:
    def __init__(self, rooms_config):
        self.rooms = [Room(room_name) for room_name in rooms_config]
        print(f"House created with rooms: {', '.join(room.name for room in self.rooms)}")

    def show_rooms(self):
        print("Rooms in the house : ")
        for room in self.rooms:
            print(f" - {room.name}")

    def __del__(self):
        print("House is being demolished. All rooms will be removed.")

house_config = ["Living Room", "Bedroom", "Kitchen", "Bathroom"]
my_house = House(house_config)
my_house.show_rooms()

del my_house
