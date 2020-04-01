from datetime import time
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

loaded_distance_graph, loaded_location_hash = distance_graph.load_graph()

# Ask user for a time to view the status of the packages at that time
while True:
    try:
        print("Please specify a time to view the status of deliver: ")
        user_am_pm = input("am or pm? ")
        user_hour = input("Hour of day? ")
        user_minute = input("Minute of day? ")
        user_option = -1

        if (0 < int(user_hour) < 13) and (-1 < int(user_minute) < 60) and (user_am_pm == "am" or user_am_pm == "pm"):
            break
        else:
            print("Please enter a correct time")
            print()
    except ValueError:
        print("Please enter a correct time")
        print()

print()

while True:
    try:
        # Ask for an option from the user. If the option is not 1 through 4 then repeat question
        print("Select an option from below for specified time -", time(int(user_hour), int(user_minute)).strftime("%I:%M"), user_am_pm)
        print("1 - View status of package by ID")
        print("2 - View status of all packages")
        print("3 - End program")
        print()

        user_option = int(input("Select option: "))

        if user_option == 1:
            print("User selected 1")
            break
        elif user_option == 2:
            print("User selected 2")
            truck_routes = TruckRoutes(loaded_package_table, loaded_distance_graph, loaded_location_hash)
            truck_routes.route_trucks(user_hour, user_minute)
            break
        elif user_option == 3:
            print("Thank you for visiting. See you again soon!")
            break
        else:
            print("Oops! That was not a valid number")
            print()
    except ValueError:
        print("Oops! That was not a valid number")
        print()


