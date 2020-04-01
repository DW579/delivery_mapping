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