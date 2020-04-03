from datetime import time
from PackageHashTable import PackageHashTable
from DistanceGraph import DistanceGraph
from TruckRoutes import TruckRoutes

print()
print("WGU C950 Performance Assessment")
print("Dustin Wurtz - ID #000791342")
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
        user_hour = int(input("Hour of day? "))
        user_minute = int(input("Minute of day? "))
        user_option = -1

        user_am_pm.lower()

        if (0 < user_hour < 13) and (-1 < user_minute < 60) and (user_am_pm == "am" or user_am_pm == "pm"):
            if user_am_pm == "am" and user_hour < 8:
                print("Please enter a time after 08:00 AM, as the trucks have not left the hub yet")
                print()
            elif user_am_pm == "pm" and user_hour < 12:
                user_hour += 12
                break
            else:
                break
        else:
            print("Please enter a correct time")
            print()
    except ValueError:
        print("Please enter a correct time")
        print()

print()

truck_routes = TruckRoutes(loaded_package_table, loaded_distance_graph, loaded_location_hash)
first_truck_mileage, second_truck_mileage, first_truck_total, second_truck_total = truck_routes.route_trucks(user_hour, user_minute)

print("First truck traveled", round(first_truck_mileage, 1), "miles and delivered", first_truck_total, "total packages")
print("Second truck traveled", round(second_truck_mileage, 1), "miles and delivered", second_truck_total, "total packages")
print("Total mileage of the two trucks:", round(first_truck_mileage, 1) + round(second_truck_mileage, 1))

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
            while True:
                try:
                    user_id = input("Please specify a package id: ")

                    if 0 < int(user_id) < 41:
                        package_table.print_package_by_id(user_id)
                        break
                    else:
                        print("Not a valid package id")
                        print()
                except ValueError:
                    print("Not a valid package id")
                    print()
            break
        elif user_option == 2:
            package_table.print_all()
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


