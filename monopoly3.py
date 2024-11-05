# 1. Name:
#      Jaxon Powell
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This program is meant to ask for user input and determine if you can buy
#      houses and hotels in monopoly. It also determines how many you can buy 
#      based on the cash that you have. 
# 4. What was the hardest part? Be as specific as possible.
#      Was it the syntax of Python?
#       The hardest part was figuring out how to get everything to work together
#       I ended up using a lot of function to make everything eaiser to see.
#      Was it an aspect of the problem you are to solve?
#       Part of the problem was figuring out how many houses or hotels are already on the 
#       property and how many more can be placed.
#      Was it the instructions or any part of the problem definition?
#       I thought these instructions were very confusing. I tried to use the flowchart that 
#       was posted last week for last weeks lab, and I thought that it was very hard to follow
#       I really didn't feel like it matched up with the instructions for this weeks assignment.
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-
#       This assignment took me 4.5 hours to complete



def get_color_group():
    return input("Do you have all of the green properties (y/n) ")

def get_houses_on_property(property_name):
    return int(input(f"How many houses are on {property_name} "
                     "(0: no houses, 1: one house ... 5: one hotel) "))

def get_available_hotels():
    return int(input("How many hotels are there to purchase: "))

def calculate_houses_needed(houses):
    return [abs(house - 5) for house in houses]

def get_cash_available():
    return int(input("How much cash do you have available: "))

def get_available_houses():
    return int(input("How many houses are there available to buy: "))

def get_houses_to_buy(max_houses, property_name):
    return int(input(f"How many houses do you want to buy on {property_name} "
                     f"(max: {max_houses}) "))

def print_purchase_info(total_houses, total_cost):
    print(f"The total cost is {total_cost}")
    print(f"The total number of houses needed is {total_houses}")
    print(f"This will cost {total_cost + 200}")
    print(f"Purchase 1 hotel and {total_houses}")
    print("Put 1 hotel on Pennsylvania and return any houses to the bank.")

def print_house_placement(nc_houses, pc_houses):
    print(f"Put {nc_houses} houses on North Carolina Avenue")
    print(f"Put {pc_houses} houses on Pacific Avenue")

def process_turn():
    if get_color_group() == "y":
        houses = [get_houses_on_property(prop) for prop in 
                  ["Pennsylvania Avenue", "North Carolina Avenue", "Pacific Avenue"]]
        
        if all(house < 5 for house in houses):
            if get_available_hotels() > 0:
                houses_needed = calculate_houses_needed(houses)
                total_houses_needed = sum(houses_needed)
                total_cost = total_houses_needed * 200
                
                if get_cash_available() >= 200:
                    if get_available_houses() >= 1:
                        print_purchase_info(total_houses_needed, total_cost)
                        
                        for i, prop in enumerate(["North Carolina", "Pacific Avenue"]):
                            if houses_needed[i+1] > 0:
                                get_houses_to_buy(houses_needed[i+1], prop)
                        
                        print_house_placement(houses_needed[1], houses_needed[2])
                    else:
                        print("There are not enough available houses.")
                else:
                    print("Sorry, you don't have enough cash to buy the needed "
                          "houses or hotels")
            else:
                print("Sorry, there are no hotels available.")
        elif houses[2] == 5:
            print("Swap houses on Pennsylvania with houses on Pacific Avenue.")
        elif houses[1] == 5:
            print("Swap houses on Pennsylvania with houses on North Carolina Avenue.")
        else:
            print("You already have a hotel on that property.")
    else:
        print("You must own all of the properties of the same color group")

def main():
    print("Welcome to the Monopoly Property Manager!")
    print("This program will run continuously. Press Ctrl+C to exit.")
    
    while True:
        try:
            print("\n--- New Turn ---")
            process_turn()
            input("\nPress Enter to start a new turn, or Ctrl+C to exit...")
        except KeyboardInterrupt:
            print("\nThank you for using the Monopoly Property Manager. Goodbye!")
            break

if __name__ == "__main__":
    main()