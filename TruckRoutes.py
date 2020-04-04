from datetime import time

"""
There are two classes, Truck and TruckRoutes. The Truck class is used to create multiple Trucks with similar functions.
In the app we will be using two trucks, first_truck and second_truck. First_truck will be delivering more packages then
second_truck. When first_truck is done with it's first round of delivers it will return to the hub and pick up the last
of the packages and deliver them. TruckRoutes class will handle the delivery portion of the app.

Truck class -
__init__ - This will initialize each truck created with the basic data points that will track the progress of the truck
    and it's packages being delivered. The descriptions of the data points are below:

    self.truck_id = able to identify which truck is which
    self.packages_priority = each truck will deliver their priority packages first. Priority packages are usually the
        opens that need to be delivered before 9:00 or 10:30 am.
    self.packages_standard = these are the packages that are delivered by EOD but have to be delivered by a specific
        truck.
    self.total_packages = this will be used to make sure that we are delivering 16 packages at a time.
    self.hour = track the hour of day for the truck
    self.minute = track the minute of day for the truck
    self.sec = track the second of day for the truck
    self.current_location = be able to know at which location the truck is to determine from what point to other point
        we will need to look at in the distance_graph
    self.mileage = tracking how far each truck goes
    
deliver_priority, deliver_standard, truck_back_to_hub, deliver_all_other_packages - All of these functions are very
similar in their use but are narrowed in scope to deliver a certain sub set of packages. 

    First, within each function there is a main while loop that runs O(n) depending on how many priority packages there
    are. But deliver_standard and deliver_all_our_packages runs O(n) times depending on how many unique standard
    packages a truck needs to deliver specific to it's truck and how many packages it can take from the last list of
    packages to make up 16. These while loops can end early if it reaches the user specified time during it's delivers.
    
    Second, within in the while loop we set up two variables, lowest_address and lowest_mileage. These two variables
    will hold the next shorest location the truck will need to travel to.
    
    Third, there is a for loop that will loop through either the priority packages or the standard packages with what
    ever amount it can loop through for the last of the packages. Worst case it will loop O(n - 1) times because each
    time we start again in the for loop there is one less package to chose from. Within the for loop there is an if/else 
    statement that checks if lowest_address is None. This is just to assign the first element to lowest_address and 
    lowest_mileage. After that, it will loop through and compare all the elements until it finds the lowest.
    
    Fourth, we have now found which is the shorest distance to travel to deliver the next package. Now we calculate
    how long it will take to get there. This will allow us to see if delivering this package will put us over the 
    time that the user has selected to be the cut off time. If delivering that package will put us over, we will break
    out of the while loop and return this function. If not then we will continue on through the function.
    
    Fifth, now that we have determined that it will not take to long to deliver the next package, we will add the
    lowest_mileage to the truck's mileage and add the time to the truck that show when a package has been delivered.
    To calculate the time in both the fourth step and this step, I used a greedy algorithm to subtract the mileage by
    18, then by .3, then by .005. The reason for it is:
        
        18 miles =  1 hour
        .3 miles = 1 minute
        .005 miles = 1 second
        
    This will allow us to incrementally increase the trucks time depending on the distance traveled.
    
    Sixth, now we need to update the trucks current location to be the location of the dropped off package. Also,
    update the status of the package that is dropped off with the time it was dropped off and which truck dropped it
    off.
    
    Seventh, we will then update the truck's total_package count to keep track how many packages it has delivered and
    remove which package was deliver from it's respective list.
    
    Eighth, we will return the status of past_time out to main.py. In main.py we will know if we can deliver the next
    set of packages or if we need to end the program with not all the packages delivered dependent on what the user
    time has been selected.
"""

class Truck:
    def __init__(self):
        self.truck_id = None
        self.packages_priority = []
        self.packages_standard = []
        self.total_packages = 0
        self.hour = 0
        self.minute = 0
        self.sec = 0
        self.current_location = '4001 South 700 East'
        self.mileage = 0

    def set_truck_id(self, id):
        self.truck_id = id

    def add_all_priority(self, packages):
        self.packages_priority = packages

    def add_all_standard(self, packages):
        self.packages_standard = packages

    def add_hour(self, hour):
        self.hour += hour

    def add_minute(self, minute):
        self.minute += minute

    def add_second(self, sec):
        self.sec += sec

    def get_total_packages(self):
        return self.total_packages

    def get_hour(self):
        return self.hour

    def get_minutes(self):
        return self.minute

    def get_seconds(self):
        return self.sec

    def get_mileage(self):
        return self.mileage

    def deliver_priority(self, distance_graph, locations, package_table, user_hour, user_minute):
        past_time = False

        # O(n), n being the amount of priority packages a truck needs to deliver.
        # This while loop will break out if we reach the user specified time, so that we tell the truck to stop delivering packages.
        while len(self.packages_priority) > 0 and past_time is False:
            # lowest_address is a string number of the package id
            lowest_address = None
            lowest_mileage = -1

            # Find the next closest package drop off from current location
            for i in range(0, len(self.packages_priority)):
                if lowest_address is None:
                    lowest_address = self.packages_priority[i]
                    # location[] needs the string address in the brackets
                    lowest_mileage = float(distance_graph[locations[self.current_location]][locations[package_table[int(self.packages_priority[i]) - 1]['address']]])
                elif float(distance_graph[locations[self.current_location]][locations[package_table[int(self.packages_priority[i]) - 1]['address']]]) < lowest_mileage:
                    lowest_address = self.packages_priority[i]
                    # location[] needs the string address in the brackets
                    lowest_mileage = float(distance_graph[locations[self.current_location]][locations[package_table[int(self.packages_priority[i]) - 1]['address']]])

            # Calculate the amount of time it will take to get from current location to the next closest drop off
            closest_mileage = lowest_mileage
            closest_hour = 0
            closest_minute = 0
            closest_second = 0

            while closest_mileage >= 18:
                closest_hour += 1
                closest_mileage -= 18
            while closest_mileage >= .3:
                closest_minute += 1
                closest_mileage -= float(.3)
                closest_mileage = round(closest_mileage, 3)

                if closest_minute > 59:
                    closest_minute = 0
                    closest_hour += 1
            while closest_mileage >= .005:
                closest_second += 1
                closest_mileage -= float(.005)
                closest_mileage = round(closest_mileage, 3)

                if closest_second > 59:
                    closest_second = 0
                    closest_minute += 1

            # Break everything down into seconds and compare
            user_seconds = (user_hour * 3600) + (user_minute * 60)
            current_seconds = (self.hour * 3600) + (self.minute * 60) + self.sec
            travel_seconds = (closest_hour * 3600) + (closest_minute * 60) + closest_second

            if (current_seconds + travel_seconds) > user_seconds:
                past_time = True
                return

            # Add lowest_mileage to Truck
            self.mileage += lowest_mileage

            # Add the time taken to the closest package drop off into Truck hour, minute, second
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

            # Update current_location with lowest_address on Truck
            self.current_location = package_table[int(lowest_address) - 1]['address']

            # Update delivery_status of the package that is delivered.
            # Using the imported function time() to format the time of the truck delivered_time
            package_table[int(lowest_address) - 1]['delivery_status']['delivered'] = True
            package_table[int(lowest_address) - 1]['delivery_status']['delivered_time'] = time(self.hour, self.minute, self.sec).strftime("%I:%M:%S %p")
            package_table[int(lowest_address) - 1]['delivery_status']['which_truck'] = self.truck_id

            self.packages_priority.remove(lowest_address)
            self.total_packages += 1

        return past_time

    def deliver_standard(self, distance_graph, locations, package_table, all_other_packages, user_hour, user_minute):
        past_time = False

        while self.total_packages < 16 and past_time is False:
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

            # Calculate the amount of time it will take to get from current location to the next closest drop off
            closest_mileage = lowest_mileage
            closest_hour = 0
            closest_minute = 0
            closest_second = 0

            while closest_mileage >= 18:
                closest_hour += 1
                closest_mileage -= 18
            while closest_mileage >= .3:
                closest_minute += 1
                closest_mileage -= float(.3)
                closest_mileage = round(closest_mileage, 3)

                if closest_minute > 59:
                    closest_minute = 0
                    closest_hour += 1
            while closest_mileage >= .005:
                closest_second += 1
                closest_mileage -= float(.005)
                closest_mileage = round(closest_mileage, 3)

                if closest_second > 59:
                    closest_second = 0
                    closest_minute += 1

            # Break everything down into seconds and compare
            user_seconds = (user_hour * 3600) + (user_minute * 60)
            current_seconds = (self.hour * 3600) + (self.minute * 60) + self.sec
            travel_seconds = (closest_hour * 3600) + (closest_minute * 60) + closest_second

            if (current_seconds + travel_seconds) > user_seconds:
                past_time = True
                return

            # Add lowest_mileage to Truck
            self.mileage += lowest_mileage

            # Add the time taken to the closest package drop off into Truck hour, minute, second
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

            # Update current_location with lowest_address on Truck
            self.current_location = package_table[int(lowest_address) - 1]['address']

            # Update delivery_status of the package that is delivered
            package_table[int(lowest_address) - 1]['delivery_status']['delivered'] = True
            package_table[int(lowest_address) - 1]['delivery_status']['delivered_time'] = time(self.hour, self.minute, self.sec).strftime("%I:%M:%S %p")
            package_table[int(lowest_address) - 1]['delivery_status']['which_truck'] = self.truck_id

            # Figure out if we delete a package from standard array of all other array
            if lowest_address in self.packages_standard:
                self.packages_standard.remove(lowest_address)
            else:
                all_other_packages.remove(lowest_address)

            self.total_packages += 1

        return past_time

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

    def deliver_all_other_packages(self, distance_graph, locations, package_table, all_other_packages, user_hour, user_minute):
        past_time = False
        add_package = True

        while len(all_other_packages) > 0 and past_time is False:
            # Check to see if package 9 with change address needs to be added
            current_seconds = (self.hour * 3600) + (self.minute * 60) + self.sec

            if current_seconds > 37200 and add_package:
                package_table[8]['address'] = '410 S State St'
                all_other_packages.append('9')
                add_package = False

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

            # Calculate the amount of time it will take to get from current location to the next closest drop off
            closest_mileage = lowest_mileage
            closest_hour = 0
            closest_minute = 0
            closest_second = 0

            while closest_mileage >= 18:
                closest_hour += 1
                closest_mileage -= 18
            while closest_mileage >= .3:
                closest_minute += 1
                closest_mileage -= float(.3)
                closest_mileage = round(closest_mileage, 3)

                if closest_minute > 59:
                    closest_minute = 0
                    closest_hour += 1
            while closest_mileage >= .005:
                closest_second += 1
                closest_mileage -= float(.005)
                closest_mileage = round(closest_mileage, 3)

                if closest_second > 59:
                    closest_second = 0
                    closest_minute += 1

            # Break everything down into seconds and compare
            user_seconds = (user_hour * 3600) + (user_minute * 60)
            travel_seconds = (closest_hour * 3600) + (closest_minute * 60) + closest_second

            if (current_seconds + travel_seconds) > user_seconds:
                past_time = True
                return

            # Add lowest_mileage to Truck
            self.mileage += lowest_mileage

            # Add the time taken to the closest package drop off into Truck hour, minute, second
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

            # Update current_location with lowest_address on Truck
            self.current_location = package_table[int(lowest_address) - 1]['address']

            # Update delivery_status of the package that is delivered
            package_table[int(lowest_address) - 1]['delivery_status']['delivered'] = True
            package_table[int(lowest_address) - 1]['delivery_status']['delivered_time'] = time(self.hour, self.minute, self.sec).strftime("%I:%M:%S %p")
            package_table[int(lowest_address) - 1]['delivery_status']['which_truck'] = self.truck_id

            all_other_packages.remove(lowest_address)
            self.total_packages += 1

        return past_time

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

        # Set truck ID
        first_truck.set_truck_id('1')
        second_truck.set_truck_id('2')

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
        past_time = first_truck.deliver_priority(distance_graph, locations, package_table, user_hour, user_minute)
        if past_time is False:
            standard_past = first_truck.deliver_standard(distance_graph, locations, package_table, all_other_packages, user_hour, user_minute)

        # Second Truck starts delivering at 9:05 AM. It will deliver priority packages first then standard
        past_time_two = second_truck.deliver_priority(distance_graph, locations, package_table, user_hour, user_minute)
        if past_time_two is False:
            second_truck.deliver_standard(distance_graph, locations, package_table, all_other_packages, user_hour, user_minute)

        # Bring the first_truck back to the hub
        # Find mileage back to the hub and add to first_trucks mileage
        if past_time is False and standard_past is False:
            first_truck.truck_back_to_hub(distance_graph, locations)

        # Deliver the rest of the packages
        if past_time is False and standard_past is False:
            all_other_past = first_truck.deliver_all_other_packages(distance_graph, locations, package_table, all_other_packages, user_hour, user_minute)

        return first_truck.get_mileage(), second_truck.get_mileage(), first_truck.get_total_packages(), second_truck.get_total_packages()

    def print(self):
        print(self.package_table)
        print(self.distance_graph)
        print(self.location_hash)