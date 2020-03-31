class Truck:
    def __init__(self):
        self.packages = []
        self.hour = 0
        self.minute = 0
        self.sec = 0
        self.current_location = None
        self.mileage = 0

    def add_package(self, package):
        self.packages.append(package)

    def add_time(self, hour, minute, sec):
        self.hour += hour
        self.minute += minute
        self.sec += sec

    def update_location(self, location):
        self.current_location = location

    def add_mileage(self, mileage):
        self.mileage += mileage

    def print_all(self):
        print(self.packages, self.hour, self.minute, self.sec, self.current_location, self.mileage)


class TruckRoutes:
    def __init__(self, loaded_package_table, loaded_distance_graph, loaded_location_hash):
        self.package_table = loaded_package_table
        self.distance_graph = loaded_distance_graph
        self.location_hash = loaded_location_hash
        package_table = self.package_table
        distance_graph = self.distance_graph
        location_hash = self.location_hash

    def route_trucks(self, user_time):
        print(user_time)
        first_truck = Truck()
        print(first_truck)

        # Set first truck array to load priority packages
        first_truck_packages = []
        # Set second truck array to load leaving late packages
        second_truck_packages = []
        # Set third truck array to load last packages
        # Set user time: hour, min, sec
        user_hour = 15
        user_min = 50
        # Set time for first truck: hour, min, sec
        # Set time for second truck: hour, min, sec
        # Set time for third truck: hour, min, sec
        # Set current location for first truck
        # Set current location for second truck
        # Set current location for third truck
        # Set variable for mileage of first truck
        # Set variable for mileage of second truck
        # Set variable for mileage of third truck

        # Load first truck array with manually selected packages from csv

        # Load second truck array with manually selected packages from csv

        # *Figure out how to load third truck, because third truck is just the first truck

        # Finish loading the first truck with additional packages to reach 16 with still shortest routes

        # Then finish loading the second truck with additional packages to reach 16 with still shortest routes

        # Run first truck starting at 8:00am until the user time
            # When package delivered, update package_table

        # Run second truck starting at 9:05am until the user time
            # When package delivered, update package_table

        # *Figure out how to run the third truck



    def print(self):
        print(self.package_table)
        print(self.distance_graph)
        print(self.location_hash)