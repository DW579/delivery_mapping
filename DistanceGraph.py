import csv


class DistanceGraph:
    def __init__(self):
        # Graph is an array of arrays that will hold the distance from one location to another
        self.graph = []
        # Hash table for quick look up to know the location of the address in the graph by it's column and row
        self.location_hash = {}

    def load_graph(self):
        # Import in distance data from csv and format it to be read
        with open('data/distance_data.csv') as csv_file:
            csv_reader = csv.reader(csv_file)

            # Read each line of the distance csv file
            for row in csv_reader:
                # Do not print the file_type line
                if row[0] != '\ufefffile_type':
                    # Creating location_hash for quick look up
                    if row[0] == '4001 South 700 East':
                        for i in range(0, len(row)):
                            self.location_hash[row[i]] = i
                    else:
                        # Appending initial distance between locations from csv file
                        self.graph.append(row)

            # Floyd-Warshall algorithm
            # Run time is O(n^3)
            for k in range(0, 27):
                for i in range(0, 27):
                    for j in range(0, 27):
                        if float(self.graph[i][k]) + float(self.graph[k][j]) < float(self.graph[i][j]):
                            num = round(float(self.graph[i][k]) + float(self.graph[k][j]), 1)
                            self.graph[i][j] = str(num)

        return self.graph, self.location_hash

    def print_graph(self):
        for row in self.graph:
            print(row)

    def test_multi_truck(self, package_table):
        package_address_arr = []
        truck_one = []
        truck_two = []
        truck_three = []

        # Loop and load all packages into one array
        for package in package_table:
            package_address_arr.append(package['address'])

        # Loop and load two trucks with 16 packages each. Truck 1 will have the shortest path and truck 2 will have the longer route
        for address in package_address_arr:
            if len(truck_one) < 16:
                truck_one.append(address)
            elif len(truck_two) < 16:
                truck_two.append(address)
            else:
                truck_three.append(address)

        # Use the algorithm I created below for test_truck on the two trucks. Return the two arrays.
        return truck_one, truck_two, truck_three

    def test_truck(self, truck_1_packages, truck_2_packages, truck_3_packages):
        distance_graph = self.graph
        locations = self.location_hash
        pri_mileage = 0
        # sec_mileage = 0
        pri_packages = ['195 W Oakland Ave', '2010 W 500 S', '4300 S 1300 E', '4580 S 2300 E', '4580 S 2300 E', '177 W Price Ave', '3595 Main St', '3595 Main St', '1330 2100 S', '300 State St', '4580 S 2300 E', '380 W 2880 S']
        sec_packages = truck_2_packages
        current_location = '4001 South 700 East'
        current_hour = 8
        current_min = 0
        current_sec = 0

        # While pri_packages is not empty, continue looping
        while len(pri_packages) > 0:
            # Set lowest_address = None
            lowest_address = None
            # Set lowest_mileage = -1
            lowest_mileage = -1

            # Loop through the remining addresses in pri_packages and find the location that is shortest to the current_location
            for i in range(0, len(pri_packages)):
                # If lowest_address is None, then set lowest_address to the selected address in pri_packages
                if lowest_address is None:
                    lowest_address = pri_packages[i]
                    lowest_mileage = float(distance_graph[locations[current_location]][locations[pri_packages[i]]])
                #Else if selected pri_packages address has a shorted travel time then what is saved in lowest_mileage, set lowest_address and lowest_mileage to the selected address in pri_packages
                elif float(distance_graph[locations[current_location]][locations[pri_packages[i]]]) < lowest_mileage:
                    lowest_address = pri_packages[i]
                    lowest_mileage = float(distance_graph[locations[current_location]][locations[pri_packages[i]]])

            # Add lowest_mileage to pri_mileage
            pri_mileage += lowest_mileage
            # Calculate the time to be added to current_hour, current_min, and current_sec
            print(lowest_address)
            print(lowest_mileage)
            while lowest_mileage >= 18:
                current_hour += 1
                lowest_mileage -= 18
                print(lowest_mileage)
            while lowest_mileage >= .3:
                current_min += 1
                lowest_mileage -= float(.3)
                lowest_mileage = round(lowest_mileage, 3)
                print(lowest_mileage)

                if current_min > 59:
                    current_min = 0
                    current_hour += 1
            while lowest_mileage >= .005:
                current_sec += 1
                lowest_mileage -= float(.005)
                lowest_mileage = round(lowest_mileage, 3)
                print(lowest_mileage)

                if current_sec > 59:
                    current_sec = 0
                    current_min += 1
            # Update current_location with lowest_address
            current_location = lowest_address
            # Remove address in lowest_address from pri_packages
            print("Delivered at: ", current_hour, ":", current_min, ":", current_sec)
            pri_packages.remove(lowest_address)

        print(pri_mileage)