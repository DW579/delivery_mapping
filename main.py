# import csv
from PackageHashTable import PackageHashTable
from DistanceGraph import DistanceGraph
from TruckRoutes import TruckRoutes

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

# TruckRoutes does the heavy lifting to figure out which route is the shortest
truck_routes = TruckRoutes(loaded_package_table, loaded_distance_graph, loaded_location_hash)
truck_routes.print()

# truck_1_addresses, truck_2_addresses, truck_3_addresses = distance_graph.test_multi_truck(loaded_package_table)
# distance_graph.test_truck(truck_1_addresses, truck_2_addresses, truck_3_addresses)
# distance_graph.print_graph()


