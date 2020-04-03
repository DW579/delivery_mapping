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
                    obj['weight'] = row[6]
                    obj['delivery_status'] = {'delivered': False, 'delivered_time': None, 'which_truck': None}

                    # Set filled object into the i-th place
                    self.table[i] = obj

                    i += 1

        return self.table

    def print_package_by_id(self, id):
        if self.table[int(id) - 1]['delivery_status']['delivered'] is True:
            print()
            print("Package", self.table[int(id) - 1]['id'], "was delivered before", self.table[int(id) - 1]['delivery_deadline'], "at", self.table[int(id) - 1]['delivery_status']['delivered_time'], "by truck", self.table[int(id) - 1]['delivery_status']['which_truck'])
        else:
            print()
            print("Package", self.table[int(id) - 1]['id'], "is en route to destination")

    # Print all the loaded packages in the hash table
    def print_all(self):
        print(" ID | ")
        print("----")
        for row in self.table:
            if row['delivery_status']['delivered'] is True:
                print("Package", row['id'], "was delivered before", row['delivery_deadline'], "at", row['delivery_status']['delivered_time'], "by truck", row['delivery_status']['which_truck'])
            else:
                print("Package", row['id'], "is en route to destination")