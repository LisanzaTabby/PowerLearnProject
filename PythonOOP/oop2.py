#question 2
# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Subclass 1
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

# Subclass 2
class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

# Subclass 3
class Bicycle(Vehicle):
    def move(self):
        print("🚴 The bicycle is being pedalled on the path.")

# Subclass 4
class Boat(Vehicle):
    def move(self):
        print("🚢 The boat is being sailed on water.")

# Polymorphism in action
def show_movement(vehicle):
    vehicle.move()

# Create objects
car = Car()
plane = Plane()
bicycle = Bicycle()
boat = Boat()

# Use the same function with different objects
for v in [car, plane, bicycle, boat]:
    show_movement(v)
