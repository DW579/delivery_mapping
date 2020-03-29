# import csv
from PackageHashTable import PackageHashTable
from DistanceGraph import DistanceGraph

# Create hash table for packages and distance graph for locations
package_table = PackageHashTable()
distance_graph = DistanceGraph()

package_table.load_table()
package_table.print_all()

distance_graph.print_graph()


