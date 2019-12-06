# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# Base Class
class Vehicle:
    pass

class GroundVehicle(Vehicle): # inherits from Vehicle
    pass

class Car(GroundVehicle): # inherits from Groundvehicle
    pass

class Motorcycle(GroundVehicle): # inherits from Groundvehicle
    pass

class FlightVehicle(Vehicle): # inherits from Vehicle
    pass

class Airplane(FlightVehicle): # inherits from FlightVehicle
    pass

class Starship(FlightVehicle): # inherits from FlightVehicle
    pass