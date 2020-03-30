# import csv
from PackageHashTable import PackageHashTable
from DistanceGraph import DistanceGraph

# Create hash table for packages and distance graph for locations
package_table = PackageHashTable()
distance_graph = DistanceGraph()

loaded_package_table = package_table.load_table()
# package_table.print_all()

distance_graph.load_graph()
distance_graph.test_multi_truck(loaded_package_table)
# distance_graph.test_truck()
# distance_graph.print_graph()


