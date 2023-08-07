# The following is a class of trucks that will deliver packages.

class Truck:
    def __init__(self, capacity, speed, load, packages, mileage, address, depart_time):
        self.truck_capacity = capacity
        self.truck_speed = speed
        self.truck_load = load
        self.truck_packages = packages
        self.truck_mileage = mileage
        self.truck_address = address
        self.depart_time = depart_time
        self.time = depart_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s," % (self.truck_capacity, self.truck_speed, self.truck_load,
                                                self.truck_packages, self.truck_mileage, self.truck_address,
                                                self.depart_time)
