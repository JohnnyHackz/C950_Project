# The following will create a package class.

class Packages:
    def __init__(self, ID, address, city, state, zip_code, Deadline_time, package_weight, delivery_status):
        self.package_ID = ID
        self.package_address = address
        self.package_city = city
        self.package_state = state
        self.package_zipcode = zip_code
        self.Deadline_time = Deadline_time
        self.package_weight = package_weight
        self.delivery_status = delivery_status
        self.departure_time = None
        self.delivery_time = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_ID, self.package_address, self.package_city,
                                                       self.package_state, self.package_zipcode,
                                                       self.Deadline_time, self.package_weight, self.delivery_time,
                                                       self.delivery_status)

    def update_status(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:
            self.delivery_status = "Package Delivered"
        elif self.departure_time > convert_timedelta:
            self.delivery_status = "Package In route"
        else:
            self.delivery_status = "Package At Hub"
