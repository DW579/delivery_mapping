import csv

"""
The DistanceGraph class has 3 defined def to create the distance graph for shorts routes to each package drop off point.
Since the trucks can travel between from one drop off point to all other drop off point at any given time, I needed
to find a way to find the shortest path that can be taken between any given point to another. I chose to use the 
Floyd-Warshall algorithm. This algorithm focuses on one location at a time and then compares two other locations in the
graph by adding them together. If the addition of the two other locations is less then the current location the, it
swaps the lowest number in. After doing this across all the locations, it builds a graph that you can know what will be
the shortest route to another location is.

Explanation of the 3 defs of this class:

__init__ - This creates an empty array for the distance graph. This array will be filled up with n number of arrays,
that will act as the rows of the graph. Each index in the main array will be a column of locations and each array within
the main array will be a row for a specific location.
There is also a location_hash object will be used for quick look up to know an addresses column and row location.

load_graph - This function will import the data from distance_data.csv. The first part of this data was provided and
this function will fill in the second half. It will use the Floyd-Warshall algorithm to determine the shortest distance
between two location points. This algorithm has a O(n^3) run time, as it has a for loop, within a for loop, within a for 
loop After it we will then be able to use the self.graph as an array of arrays that will act as a graph with rows and 
columns. We will then be able to use the location_hash to know which row and column a certain location can be found. 

Examples of self.graph and self.location_hash after load_graph is finished:

self.location_hash - 
{
    '4001 South 700 East': 0,
    '1060 Dalton Ave S': 1,
    '1330 2100 S': 2,
    ...
}

self.graph -
[
    ['0', '7.2', '3.8', '7.0', '2.2', '3.5', '8.8', '6.7', '7.5', '2.8', '6.4', '3.2', '7.5', '5.1', '4.2', '3.6', '3.6', '2', '3.6', '6.5', '1.9', '3.4', '2.4', '6.4', '2.4', '5', '3.6'],
    ['7.2', '0', '7.1', '6.4', '6', '4.8', '1.6', '2.8', '4.8', '6.3', '7.3', '5.3', '4.8', '3', '4.3', '4.5', '5.9', '6', '5', '4.8', '9.0', '10.6', '8.3', '6.9', '9.6', '4.4', '10.8'],
    ...
]

Therefore, using both the graph and location_hash, we can see that the shortest travel time between the location
'1060 Dalton Ave S', which is row 1, to location '1330 2100 S', which is column 2, is 7.1.

print_graph - This function will print each row of the self.graph. During debugging this was used to make sure
load_graph with the Floyd-Warshall algorithm was working correctly. It has a run time of O(n) to print out each row of
the graph.
"""


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

            # Read each line of the distance_data.csv file
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
        # O(n)
        for row in self.graph:
            print(row)