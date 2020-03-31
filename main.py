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

# TruckRoutes does the heavy lifting to figure out which route is the shortest
truck_routes = TruckRoutes(loaded_package_table, loaded_distance_graph, loaded_location_hash)
truck_routes.route_trucks(user_time)
truck_routes.print()

# distance_graph.test_truck()
# distance_graph.print_graph()


