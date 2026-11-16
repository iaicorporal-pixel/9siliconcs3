# 1. Answer the following questions:
#
# a. What is duck typing, as explained in the video?
# Answer: Duck typing is a concept in Python where an object's suitability is 
# determined by the methods and attributes it has, rather than its actual class 
# or inheritance. ("If it walks like a duck and quacks like a duck, it is a duck.")
#
# b. What did the Car class need to have so it could work inside the same loop 
# as Dog and Cat, even if it does not inherit from the Animal class?
# Answer: The Car class needed to have a speak() method (the exact same method 
# name called inside the loop) and any required attributes (like alive = True) 
# that Dog and Cat use.
# ---------------------------------------------------------


# 2. Create the Python code:

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

my_car = Car()
my_boat = Boat()
my_drone = Drone()

start_trip(my_car)
start_trip(my_boat)
start_trip(my_drone)


# ---------------------------------------------------------
# 3. How does the code in 2.2 demonstrate polymorphism?
# Answer: Even though Car, Boat, and Drone do not share a parent class, they all 
# implement the same move() method interface. This allows the single start_trip() 
# function to treat all three different objects uniformly and execute their own 
# specific versions of move().
# ---------------------------------------------------------