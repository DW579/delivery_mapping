# import csv
from PackageHashTable import PackageHashTable
from DistanceGraph import DistanceGraph
from TruckRoutes import TruckRoutes

time_format_incorrect = True

print()
print("Dustin Wurtz - ID #000791342")
print("WGU C950 Performance Assessment")
print()

# Create hash table for packages and distance graph for locations
package_table = PackageHashTable()
distance_graph = DistanceGraph()

loaded_package_table = package_table.load_table()
print("Package hash table loaded")
print()

loaded_distance_graph, loaded_location_hash = distance_graph.load_graph()
print("Distance graph loaded")
print()

# Ask user for a time to view the status of the packages at that time
user_time = input("To view status of packages at a particular time, please specify: ")
user_option = -1

# Ask for an option from the user. If the option is not 1 through 4 then repeat question
while user_option < 1 or user_option > 4:
    print("Select an option from below for time - ", user_time)
    print("1 - View status of package by ID")
    print("2 - View status of all packages")
    print("3 - Enter new time")
    print("4 - End program")

    user_option = int(input("Select option: "))


# TruckRoutes does the heavy lifting to figure out which route is the shortest
truck_routes = TruckRoutes(loaded_package_table, loaded_distance_graph, loaded_location_hash)
truck_routes.route_trucks(user_time)
# truck_routes.print()

package_table.print_all()

# distance_graph.test_truck()
# distance_graph.print_graph()


