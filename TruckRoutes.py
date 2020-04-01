from datetime import time


class Truck:
    def __init__(self):
        self.packages_priority = []
        self.packages_standard = []
        self.total_packages = 0
        self.hour = 0
        self.minute = 0
        self.sec = 0
        self.current_location = '4001 South 700 East'
        self.mileage = 0

    def get_all_priority(self):
        return self.packages_priority

    def get_all_standard(self):
        return self.packages_standard

    def get_total_package_count(self):
        return self.total_packages

    def add_total_package_count(self, num):
        self.total_packages += num

    def add_all_priority(self, packages):
        self.packages_priority = packages

    def add_all_standard(self, packages):
        self.packages_standard = packages

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

    def deliver_priority(self, distance_graph, locations, package_table):
        while len(self.packages_priority) > 0:
            # lowest_address is a string number of the package id
            lowest_address = None
            lowest_mileage = -1

            # Loop through the remining addresses in pri_packages and find the location that is shortest to the current_location
            for i in range(0, len(self.packages_priority)):
                if lowest_address is None:
                    lowest_address = self.packages_priority[i]
                    # location[] needs the string address in the brackets
                    lowest_mileage = float(distance_graph[locations[self.current_location]][locations[package_table[int(self.packages_priority[i]) - 1]['address']]])
                elif float(distance_graph[locations[self.current_location]][locations[package_table[int(self.packages_priority[i]) - 1]['address']]]) < lowest_mileage:
                    lowest_address = self.packages_priority[i]
                    # location[] needs the string address in the brackets
                    lowest_mileage = float(distance_graph[locations[self.current_location]][locations[package_table[int(self.packages_priority[i]) - 1]['address']]])

            # Add lowest_mileage to first_truck
            self.mileage += lowest_mileage

            # Calculate the time to be added to first_truck. Using a greedy algorithm to break down the addition of time
            while lowest_mileage >= 18:
                self.hour += 1
                lowest_mileage -= 18
            while lowest_mileage >= .3:
                self.minute += 1
                lowest_mileage -= float(.3)
                lowest_mileage = round(lowest_mileage, 3)

                if self.minute > 59:
                    self.minute = 0
                    self.hour += 1
            while lowest_mileage >= .005:
                self.sec += 1
                lowest_mileage -= float(.005)
                lowest_mileage = round(lowest_mileage, 3)

                if self.sec > 59:
                    self.sec = 0
                    self.minute += 1

            # Update current_location with lowest_address on first_truck
            self.current_location = package_table[int(lowest_address) - 1]['address']

            print("Package ID: ", lowest_address)

            # Update delivery_status of the package that is delivered
            package_table[int(lowest_address) - 1]['delivery_status']['delivered'] = True
            package_table[int(lowest_address) - 1]['delivery_status']['delivered_time'] = time(self.hour, self.minute, self.sec).strftime("%I:%M:%S %p")

            print(package_table[int(lowest_address) - 1])

            self.packages_priority.remove(lowest_address)
            self.total_packages += 1

        print(self.mileage)

    def deliver_standard(self, distance_graph, locations, package_table, all_other_packages):
        while self.total_packages < 16:
            # lowest_address is a string number of the package id
            lowest_address = None
            lowest_mileage = -1

            if len(self.packages_standard) > 0:
                # First loop through first trucks standard packages then loop through all_other_packages
                for i in range(0, len(self.packages_standard)):
                    if lowest_address is None:
                        lowest_address = self.packages_standard[i]
                        # location[] needs the string address in the brackets
                        lowest_mileage = float(distance_graph[locations[self.current_location]][locations[package_table[int(self.packages_standard[i]) - 1]['address']]])
                    elif float(distance_graph[locations[self.current_location]][locations[package_table[int(self.packages_standard[i]) - 1]['address']]]) < lowest_mileage:
                        lowest_address = self.packages_standard[i]
                        # location[] needs the string address in the brackets
                        lowest_mileage = float(distance_graph[locations[self.current_location]][locations[package_table[int(self.packages_standard[i]) - 1]['address']]])
            else:
                for i in range(0, len(all_other_packages)):
                    if lowest_address is None:
                        lowest_address = all_other_packages[i]
                        # location[] needs the string address in the brackets
                        lowest_mileage = float(distance_graph[locations[self.current_location]][locations[package_table[int(all_other_packages[i]) - 1]['address']]])
                    elif float(distance_graph[locations[self.current_location]][locations[package_table[int(all_other_packages[i]) - 1]['address']]]) < lowest_mileage:
                        lowest_address = all_other_packages[i]
                        # location[] needs the string address in the brackets
                        lowest_mileage = float(distance_graph[locations[self.current_location]][locations[package_table[int(all_other_packages[i]) - 1]['address']]])

            # Add lowest_mileage to first_truck
            self.mileage += lowest_mileage

            # Calculate the time to be added to first_truck. Using a greedy algorithm to break down the addition of time
            while lowest_mileage >= 18:
                self.hour += 1
                lowest_mileage -= 18
            while lowest_mileage >= .3:
                self.minute += 1
                lowest_mileage -= float(.3)
                lowest_mileage = round(lowest_mileage, 3)

                if self.minute > 59:
                    self.minute = 0
                    self.hour += 1
            while lowest_mileage >= .005:
                self.sec += 1
                lowest_mileage -= float(.005)
                lowest_mileage = round(lowest_mileage, 3)

                if self.sec > 59:
                    self.sec = 0
                    self.minute += 1

            # Update current_location with lowest_address on first_truck
            self.current_location = package_table[int(lowest_address) - 1]['address']

            print("Package ID: ", lowest_address)

            # Update delivery_status of the package that is delivered
            package_table[int(lowest_address) - 1]['delivery_status']['delivered'] = True
            package_table[int(lowest_address) - 1]['delivery_status']['delivered_time'] = time(self.hour, self.minute, self.sec).strftime("%I:%M:%S %p")

            print(package_table[int(lowest_address) - 1])

            if lowest_address in self.packages_standard:
                self.packages_standard.remove(lowest_address)
            else:
                all_other_packages.remove(lowest_address)

            self.total_packages += 1

        print(self.mileage)

    def truck_back_to_hub(self, distance_graph, locations):
        mileage_to_hub = float(distance_graph[locations[self.current_location]][locations['4001 South 700 East']])
        self.mileage += mileage_to_hub

        # Add time to first_trucks from mileage
        # Calculate the time to be added to first_truck. Using a greedy algorithm to break down the addition of time
        while mileage_to_hub >= 18:
            self.hour += 1
            mileage_to_hub -= 18
        while mileage_to_hub >= .3:
            self.minute += 1
            mileage_to_hub -= float(.3)
            mileage_to_hub = round(mileage_to_hub, 3)

            if self.minute > 59:
                self.minute = 0
                self.hour += 1
        while mileage_to_hub >= .005:
            self.sec += 1
            mileage_to_hub -= float(.005)
            mileage_to_hub = round(mileage_to_hub, 3)

            if self.sec > 59:
                self.sec = 0
                self.minute += 1

    def deliver_all_other_packages(self, distance_graph, locations, package_table, all_other_packages):
        # Deliver the rest of the packages from all_other_packages
        while len(all_other_packages) > 0:
            # lowest_address is a string number of the package id
            lowest_address = None
            lowest_mileage = -1

            # Loop through the remining addresses in pri_packages and find the location that is shortest to the current_location
            for i in range(0, len(all_other_packages)):
                if lowest_address is None:
                    lowest_address = all_other_packages[i]
                    # location[] needs the string address in the brackets
                    lowest_mileage = float(distance_graph[locations[self.current_location]][locations[package_table[int(all_other_packages[i]) - 1]['address']]])
                elif float(distance_graph[locations[self.current_location]][locations[package_table[int(all_other_packages[i]) - 1]['address']]]) < lowest_mileage:
                    lowest_address = all_other_packages[i]
                    # location[] needs the string address in the brackets
                    lowest_mileage = float(distance_graph[locations[self.current_location]][locations[package_table[int(all_other_packages[i]) - 1]['address']]])

            # Add lowest_mileage to first_truck
            self.mileage += lowest_mileage

            # Calculate the time to be added to first_truck. Using a greedy algorithm to break down the addition of time
            while lowest_mileage >= 18:
                self.hour += 1
                lowest_mileage -= 18
            while lowest_mileage >= .3:
                self.minute += 1
                lowest_mileage -= float(.3)
                lowest_mileage = round(lowest_mileage, 3)

                if self.minute > 59:
                    self.minute = 0
                    self.hour += 1
            while lowest_mileage >= .005:
                self.sec += 1
                lowest_mileage -= float(.005)
                lowest_mileage = round(lowest_mileage, 3)

                if self.sec > 59:
                    self.sec = 0
                    self.minute += 1

            # Update current_location with lowest_address on first_truck
            self.current_location = package_table[int(lowest_address) - 1]['address']

            print("Package ID: ", lowest_address)

            # Update delivery_status of the package that is delivered
            package_table[int(lowest_address) - 1]['delivery_status']['delivered'] = True
            package_table[int(lowest_address) - 1]['delivery_status']['delivered_time'] = time(self.hour, self.minute, self.sec).strftime("%I:%M:%S %p")

            print(package_table[int(lowest_address) - 1])

            all_other_packages.remove(lowest_address)
            self.total_packages += 1

    def print_all(self):
        print(self.packages_priority, self.packages_standard, self.total_packages, self.hour, self.minute, self.sec, self.current_location, self.mileage)


class TruckRoutes:
    def __init__(self, loaded_package_table, loaded_distance_graph, loaded_location_hash):
        self.package_table = loaded_package_table
        self.distance_graph = loaded_distance_graph
        self.location_hash = loaded_location_hash

    def route_trucks(self, user_hour, user_minute):
        # Reassign distance graph and locations hash to new variables, so that we don't change the initial ones
        distance_graph = self.distance_graph
        locations = self.location_hash
        package_table = self.package_table

        # Create two empty trucks
        first_truck = Truck()
        second_truck = Truck()

        # Load first truck priority and standard arrays with manual loading
        first_truck.add_all_priority(['1', '13', '14', '15', '16', '20', '21', '29', '30', '34', '40'])
        first_truck.add_all_standard(['19'])
        # Set starting time for the first truck
        first_truck.add_hour(8)
        first_truck.add_minute(0)
        first_truck.add_second(0)

        # Load second truck priority and standard arrays with manual loading
        second_truck.add_all_priority(['6', '25', '26', '31', '32', '37', '38'])
        second_truck.add_all_standard(['3', '18', '28', '36'])
        # Set starting time for the second truck
        second_truck.add_hour(9)
        second_truck.add_minute(5)
        second_truck.add_second(0)

        # All other packages that do not need to be on any specific truck
        all_other_packages = ['2', '4', '5', '7', '8', '10', '11', '12', '17', '22', '23', '24', '27', '33', '35', '39']

        # First Truck starts delivering at 8:00 AM. It will deliver priority packages first then standard
        first_truck.deliver_priority(distance_graph, locations, package_table)
        first_truck.deliver_standard(distance_graph, locations, package_table, all_other_packages)

        # Second Truck starts delivering at 9:05 AM. It will deliver priority packages first then standard
        second_truck.deliver_priority(distance_graph, locations, package_table)
        second_truck.deliver_standard(distance_graph, locations, package_table, all_other_packages)

        # Bring the first_truck back to the hub
        # Find mileage back to the hub and add to first_trucks mileage
        first_truck.truck_back_to_hub(distance_graph, locations)

        print("First truck back to the hub at: ", time(first_truck.get_hour(), first_truck.get_minutes(), first_truck.get_seconds()).strftime("%I:%M:%S %p"))

        # Deliver the rest of the packages
        first_truck.deliver_all_other_packages(distance_graph, locations, package_table, all_other_packages)

        print(first_truck.get_mileage())
        print(time(first_truck.get_hour(), first_truck.get_minutes(), first_truck.get_seconds()).strftime("%I:%M:%S %p"))
        print(second_truck.get_mileage())
        print(time(second_truck.get_hour(), second_truck.get_minutes(), second_truck.get_seconds()).strftime("%I:%M:%S %p"))

    def print(self):
        print(self.package_table)
        print(self.distance_graph)
        print(self.location_hash)