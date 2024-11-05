#Python

color_group = input("Do you have all of the green properties (y/n) ")

if color_group == "y":
    houses_on_pa = int(input("How many houses are on Pennyslvania Avenue (0: no houses, 1: one house ... 5: one hotel) "))        
    if houses_on_pa < 5:
        houses_on_nc = int(input("How many houses are on North Carolina Avenue (0: no houses, 1: one house, ... 5: one hotel) "))
        if houses_on_nc < 5:
            houses_on_pc = int(input("How many houses are on Pacific Avenue (0: no houses, 1: one house, ... 5: one hotel) "))
            if houses_on_pc < 5:
                avaliable_hotels = int(input("How many hotels are there to purchase: "))
                if avaliable_hotels > 0:
                    number_houses_pa_needs = houses_on_pa - 5
                    number_houses_nc_needs = houses_on_nc - 5
                    number_houses_pc_needs = houses_on_pc - 5  
                    house_that_pa_needs = abs(number_houses_pa_needs)
                    house_that_nc_needs = abs(number_houses_nc_needs)
                    house_that_pc_needs = abs(number_houses_pc_needs)
                    number_houses_total_needed =  number_houses_pa_needs + number_houses_nc_needs + number_houses_pc_needs
                    number_houses_total_needed = abs(number_houses_total_needed)
                    total_money_needed = number_houses_total_needed * 200
                    cash_avaliable = int(input("How much cash do you have avaliable: "))
                    if cash_avaliable >= 200:
                        avaliable_houses = int(input("How many houses are there avaliable to buy:"))
                        if avaliable_houses >= 1:
                            print(f"The total cost is {total_money_needed}")
                            print(f"The total number of houses need is {number_houses_total_needed}")
                            if number_houses_nc_needs > 0:
                                houses_on_nc_to_buy = int(input(f"How many houses do you want to buy on North Carolina (max: {number_houses_nc_needs})"))
                            if number_houses_pc_needs > 0:
                                houses_on_pc_to_buy = int(input(f"How many houses do you want to buy on Pacific Avenue (max: {number_houses_pc_needs})"))
                            
                            print(f"This will cost {((number_houses_total_needed) * 200) + 200}")
                            print(f"Purchase 1 hotel and {number_houses_total_needed}")
                            print(f"Put 1 hotel on Pennsylvania and return any houses to the bank.")
                            print(f"Put {house_that_nc_needs} houses on North Carolina Avenue")
                            print(f"Put {house_that_pc_needs} houses on Pacific Avenue")
                        else:
                            print("There are not enough avaliable houses.")
                    else:
                        print("Sorry you dont have enough cash to buy the needed houses or hotels")
                else:
                    print("Sorry there are no hotels avaliable.")
            else:
                houses_on_pa = houses_on_pc
                print(f"Swap houses on Pennslyvania with houses on Pacific Avenue.")
        else: 
            houses_on_pa = houses_on_nc
            print(f"Swap houses Pennslyvania iwht houses on North Carolin Avenue.")
    else:
        print("You already have a hotel on that property.")
else:
    print("You must own all of the properties of the same color group")


