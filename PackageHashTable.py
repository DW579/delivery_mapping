import csv


class PackageHashTable:
    def __init__(self):
        # Set hash table with a fixed size to hold all 40 packages.
        # Creates 40 'None' in the array.
        # Package hash table storage size - O(1)
        self.table = [None] * 40

    def load_table(self):
        # Import data from packages_data.csv
        # Data used to create package hash table
        with open('data/packages_data.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Position in self.table
            i = 0

            """
            Loop through all the rows in the csv file to build package hash table.
            This table will allow for n number of packages to be set with in the table and be searched by it's index - 1.
            Each package will be an object and that object will be appended into an array. Then a particular package
            object can be searched for in O(1), constant time, by searching the package ID - 1.
            For example, if you want to search for package 5, you will need to search in the self.table array by,
            self.table[5 - 1], because arrays start at the 0 index. Since we do not have package id 0, we can not match
            up one to one the package id with the exact index location in the array.
            
            By structuring the package data into an object, it makes it for fast and easy look up for a specific data
            point of the package. Setting the key as a specific data point that is common across all packages and 
            setting it's unique value. For example, to find the address of a package with a known ID, the user simply
            searches by, table[5 - 1]['address']. That is a look up time of O(1).
            
            The Big O time loop through the package data in the csv and create a data object for each package is O(n).
            
            Basic structure of the package hash table below:
            
            [
                {
                    'id': '1',
                    'address': '195 W Oakland Ave',
                    'city': 'Salt Lake City'
                    'state': 'UT',
                    'zip': '84115',
                    'delivery_deadline': '10:30 AM',
                    'weight': '21',
                    'delivery_status': {
                                            'delivered': False,
                                            'delivered_time': None,
                                            'which_truck': None
                                        }
                },
                ...
            ]
            
            I structured the 'delivery_status' having an object as it's value due to a logic to look up the multiple
            data points that share the relationship of 'delivered', 'delivered_time', and 'which_truck' for delivery
            status.
            """
            for row in csv_reader:
                # If not header row in packages_data.csv file
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

                    # Increase position of self.table by 1
                    i += 1

        # Return the table out to main.py to be used throughout the app
        return self.table

    def print_package_by_id(self, id):
        # Function to print in the command line the delivery status of a package
        # O(1)
        if self.table[int(id) - 1]['delivery_status']['delivered'] is True:
            # If delivered print this
            print()
            print("Package", self.table[int(id) - 1]['id'], "was delivered before", self.table[int(id) - 1]['delivery_deadline'], "at", self.table[int(id) - 1]['delivery_status']['delivered_time'], "by truck", self.table[int(id) - 1]['delivery_status']['which_truck'])
        else:
            # If not delivered print this
            print()
            print("Package", self.table[int(id) - 1]['id'], "is en route to destination")

    def print_all(self):
        # Function to print all the loaded packages in the hash table
        # O(n)
        for row in self.table:
            if row['delivery_status']['delivered'] is True:
                # If delivered print this
                print("Package", row['id'], "was delivered before", row['delivery_deadline'], "at", row['delivery_status']['delivered_time'], "by truck", row['delivery_status']['which_truck'])
            else:
                # If not delivered print this
                print("Package", row['id'], "is en route to destination")