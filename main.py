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

        # Check to see if the user put in a time after 8:00 am because packages are not being delivered until then
        # Also check to see if the user provided the correct time format
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

# Setting up truck_routes to be from the class TruckRoutes and loading in the package_table, distane_graph and location_hash
truck_routes = TruckRoutes(loaded_package_table, loaded_distance_graph, loaded_location_hash)
# Returning the results of the status of both trucks on how much mileage they traveled and how many packages they delivered
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
                        # This function will work at O(1), constant time, since we know the exact ID of the package to look up
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
            # This will be O(n) times to loop through and print each package status
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


"""
Two strengths of the algorithm I chose:
    The algorithm that I chose to figure out the shortest path between two locations is the Floyd-Warshall algorithm.
    The first strength this algorithm has is that since we can travel directly from one node to any other node directly,
    we can have a quick look up of the distance from one node to another. The look up is structure as such:
    
        distance_graph[2][4]
        
    By calling the distance_graph with just specifying the index locations, it is a constant time look up, O(1).
    Therefore, after running through the Floyd-Warshall algorithm for O(n^3) we have a constant time look up.  
    The second strength is that this can scale with any number of locations and each location node does not need a 
    direct path to any other location node.
    
Does the algorithm meet all the criteria and requirements in the given scenario.
    Yes, the algorithm and the overall app does meet all requirements. The Floyd-Warshall algorithm finds the shorest
    path between each location node. The app uses that data and finds the status of each package at any specified time
    and provides that information back to the user through the command line interface.
    
Identify two other algorithms that would meet the requirements of the scenario:
    Johnson's algorithm can be used. This is different from Floyd-Warshall's in that it uses two algorithms to make it
    up. It uses the Bellman-Ford and Dijkstra's algorithms. First it uses the Bellman-Ford algorithm to find the
    shortest the shortest paths between each location node to all other location nodes. Then it will use the 
    Dijkstra's algorithm to re-weigh all the edges between the nodes, possibly to zeros and ones. This graph then can
    be used to find the shortest path between all the nodes.
    
Describe what can be differently in this project:
    A few things I can do differently. First, I could simplify both the truck and user time. Instead of tracking their 
    hours, minutes, and seconds, I should reduce those times down to just their seconds. Then I can more easily track
    and compare just the seconds. Second, I could simplify the greedy algorithm that figures out the time it will take
    to travel the distance between two locations. I could use division and modular equation to figure that part out,
    which would make it constant time. Third, I would simplify the functions in the TruckRoutes class so that I am
    not repeating alot of the same code for it's functions, deliver_priority, deliver_standard, truck_back_to_hub, 
    and deliver_all_other_packages.
    
Verify the data structure you chose meets all the requirements:
    Yes, the data structure I used for the distance graph and package table do meet all the requirements. Specifically,
    the package table is an array of objects. I do not use any class or any built in python function to look up the
    data of a package. A package can be found by subtracting 1 from the id and that is it's index location in the 
    array. Then since the package is an object, you can find the value of any key in constant time. Look up time for
    both finding the package in the array and the value of a key are both constant time, if both id and data point are
    known.
    
    This allows the package table to be scalable to accommodate more packages. It still gives the look up time of
    O(1) if the package id is known. Although, if the package ID is not known and you want to know which package has
    a certain address, it will be O(n) time to loop through the array to find the package.

Describe two other data structures that can be used:
    Another data structure that can be used is a linked list. Linked list allow a better way to use memory. Instead,
    for instantiating a fixed array in memory we could create nodes that are connected by a linked list and each
    node can be stored randomly throughout the computer memory. But this will always have a look up time of O(n)
    because in a linked list you can not look up a known node id in constant time but have to loop through the 
    linked list each time.
    
    Another data structure is a hash table. In which we can do a constant look up time of each package id. Although,
    if we don't know the id of a package and want to know all packages with the same address, we would need to 
    loop through the hash table at O(n).
"""


