import csv


class PackageHashTable:
    def __init__(self):
        # Set hash table with a fixed size to hold all 40 packages.
        # Creates 40 'None' in the array.
        # Package hash table storage size - O(n) or O(40)
        self.table = [None] * 40

    def load_table(self):
        with open('data/packages_data.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Position in self.table
            i = 0

            # Loop through all the rows in the csv file
            for row in csv_reader:
                # If not header row
                if row[0] != '\ufeffid':
                    # New object created for each package and it's data
                    obj = {}

                    # Setting individual data points into the object for each package
                    obj['id'] = row[0]
                    obj['address'] = row[1]
                    obj['city'] = row[2]
                    obj['state'] = row[3]
                    obj['zip'] = row[4]
                    obj['delivery_deadline'] = row[5]
                    obj['mass'] = row[6]
                    obj['delivered'] = False
                    obj['delivered_time'] = None

                    # Set filled object into the i-th place
                    self.table[i] = obj

                    i += 1

    # Print all the loaded packages in the hash table
    def print_all(self):
        print(self.table)