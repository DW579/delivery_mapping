from datetime import time


class Truck:
    def __init__(self):
        self.packages_priority = []
        self.packages_standard = []
        self.total_packages = 0
        self.hour = 0
        self.minute = 0
        self.sec = 0
        self.current_location = None
        self.mileage = 0

    def get_all_priority(self):
        return self.packages_priority

    def get_all_standard(self):
        return self.packages_standard

    def add_all_priority(self, packages):
        self.packages_priority = packages
        self.total_packages += len(packages)

    def add_all_standard(self, packages):
        self.packages_standard = packages
        self.total_packages += len(packages)

    def add_standard(self, package):
        self.packages_standard.append(package)
        self.total_packages += 1

    def priority_length(self):
        return len(self.packages_priority)

    def standard_length(self):
        return len(self.packages_standard)

    def remove_priority(self, package):
        self.packages_priority.remove(package)

    def remove_standard(self, package):
        self.packages_standard.remove(package)

    def add_hour(self, hour):
        self.hour += hour

    def add_minute(self, minute):
        self.minute += minute

    def add_second(self, sec):
        self.sec += sec

    def get_hour(self):
        return self.hour

    def get_minutes(self):
        return self.minute

    def get_seconds(self):
        return self.sec

    def update_minutes(self, minute):
        self.minute = minute

    def update_seconds(self, second):
        self.sec = second

    def get_location(self):
        return self.current_location

    def update_location(self, location):
        self.current_location = location

    def get_mileage(self):
        return self.mileage

    def add_mileage(self, mileage):
        self.mileage = round(self.mileage + mileage, 3)

    def print_all(self):
        print(self.packages_priority, self.packages_standard, self.total_packages, self.hour, self.minute, self.sec, self.current_location, self.mileage)


class TruckRoutes:
    def __init__(self, loaded_package_table, loaded_distance_graph, loaded_location_hash):
        self.package_table = loaded_package_table
        self.distance_graph = loaded_distance_graph
        self.location_hash = loaded_location_hash

    def route_trucks(self, user_time):
        # Reassign distance graph and locations hash to new variables, so that we don't change the initial ones
        distance_graph = self.distance_graph
        locations = self.location_hash

        # Create two empty trucks
        first_truck = Truck()
        second_truck = Truck()

        # The manually loaded packages for the trucks
        first_priority = ['1', '13', '14', '15', '16', '20', '21', '29', '30', '34', '40']
        first_standard = ['19']
        second_priority = ['6', '25', '26', '31', '32', '37', '38']
        second_standard = ['3', '18', '28', '36']
        all_other_packages = ['2', '4', '5', '7', '8', '10', '11', '12', '17', '22', '23', '24', '27', '33', '35', '39']

        first_truck.print_all()

        # Set user time: hour, min, sec
        user_hour = 15
        user_min = 50

        # Load first truck priority and standard arrays with manual loading
        first_truck.add_all_priority(first_priority)
        first_truck.add_all_standard(first_standard)
        # Set starting time for the first truck
        first_truck.add_hour(8)
        first_truck.add_minute(0)
        first_truck.add_second(0)
        # Set hub as current location for first truck
        first_truck.update_location('4001 South 700 East')

        # Load second truck priority and standard arrays with manual loading
        second_truck.add_all_priority(second_priority)
        second_truck.add_all_standard(second_standard)
        # Set starting time for the second truck
        second_truck.add_hour(9)
        second_truck.add_minute(5)
        second_truck.add_second(0)
        # Set hub as current location for second truck
        second_truck.update_location('4001 South 700 East')

        # *Figure out how to load third truck, because third truck is just the first truck

        # Run first truck starting at 8:00am until the user time
        # Start delivering priority packages
        first_priority_packages = first_truck.get_all_priority()
        while len(first_priority_packages) > 0:
            # lowest_address is a string number of the package id
            lowest_address = None
            lowest_mileage = -1

            # Loop through the remining addresses in pri_packages and find the location that is shortest to the current_location
            for i in range(0, len(first_priority_packages)):
                if lowest_address is None:
                    lowest_address = first_priority_packages[i]
                    # location[] needs the string address in the brackets
                    lowest_mileage = float(distance_graph[locations[first_truck.get_location()]][locations[self.package_table[int(first_priority_packages[i]) - 1]['address']]])
                elif float(distance_graph[locations[first_truck.get_location()]][locations[self.package_table[int(first_priority_packages[i]) - 1]['address']]]) < lowest_mileage:
                    lowest_address = first_priority_packages[i]
                    # location[] needs the string address in the brackets
                    lowest_mileage = float(distance_graph[locations[first_truck.get_location()]][locations[self.package_table[int(first_priority_packages[i]) - 1]['address']]])

            # Add lowest_mileage to first_truck
            first_truck.add_mileage(lowest_mileage)

            # Calculate the time to be added to first_truck. Using a greedy algorithm to break down the addition of time
            while lowest_mileage >= 18:
                first_truck.add_hour(1)
                lowest_mileage -= 18
            while lowest_mileage >= .3:
                first_truck.add_minute(1)
                lowest_mileage -= float(.3)
                lowest_mileage = round(lowest_mileage, 3)

                if first_truck.get_minutes() > 59:
                    first_truck.update_minutes(0)
                    first_truck.add_hour(1)
            while lowest_mileage >= .005:
                first_truck.add_second(1)
                lowest_mileage -= float(.005)
                lowest_mileage = round(lowest_mileage, 3)

                if first_truck.get_seconds() > 59:
                    first_truck.update_seconds(0)
                    first_truck.add_minute(1)

            # Update current_location with lowest_address on first_truck
            first_truck.update_location(self.package_table[int(lowest_address) - 1]['address'])

            print("Package ID: ", lowest_address)

            # Update delivery_status of the package that is delivered
            self.package_table[int(lowest_address) - 1]['delivery_status']['delivered'] = True
            self.package_table[int(lowest_address) - 1]['delivery_status']['delivered_time'] = time(first_truck.get_hour(), first_truck.get_minutes(), first_truck.get_seconds()).strftime("%I:%M:%S %p")

            print(self.package_table[int(lowest_address) - 1])

            first_priority_packages.remove(lowest_address)

        print(first_truck.get_mileage())

        # Run second truck starting at 9:05am until the user time
            # When package delivered, update package_table

        # *Figure out how to run the third truck



    def print(self):
        print(self.package_table)
        print(self.distance_graph)
        print(self.location_hash)