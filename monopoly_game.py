#Python

def property_status(property_name):
    while True:
        status = input(f"What is on {property_name}: (0: no houses 1: one house ... 5: hotel)")
        if status in [1, 2, 3, 4, 5]:
            return int(status)
        print("Invalid input: please enter a number between 1 and 5")


def calculate_purchasable_amount(cash):
    can_purchase = cash / 200
    return can_purchase

#This function lets the user select the total number of houses they want to buy,
# and adds it to the respective property also selected by the user. 
def buy_house(can_purchase, avaliable_houses, pe, nc, pa):
    print(f"You are able to purchase {can_purchase} houses")
    purchased = int(input("How many houses would you like to purchase."))
    if purchased <= can_purchase and purchased <= avaliable_houses:
        print("Which property would you like to place the houses on.")
        property = input("pe: Pennsylvania Avenue, nc: North Carolina, pa: Pacific Avenue")

        pe = pe + purchased 
        nc = nc + purchased
        pa = pa + purchased

        if pe <= 4 or nc <= 4 or pa <= 4:
            if property == "pe":
                pe += purchased
            if property == "nc":
                nc += purchased
            if property == "pa":
                pa += purchased
        else:
            print("You already have the max amount of houses on that property. Buy a hotel.")
    else:
        print("You selected to many houses, you either don't have enough money,")     
        print("or there aren't enough avaliable houses.")

    return purchased, avaliable_houses, pe, nc, pa

def buy_hotel(can_purchase, avaliable_hotels):
    print("You are able to purchase {can_purchase} houses")
    purchased = int(input("How many houses would you like to purchase."))


def swap_houses():
    pass

def main():

    own_all_of_color = input("Do you own all green propetries: (y/n) ")

    if own_all_of_color.lower == "y":
        pe = property_status("Pennylysvania Avenue")
        nc = property_status("North Carolina Avenue")
        pa = property_status("Pacific Avenue")
        cash = float(input("How much cash do you have to spend: $"))
        avaliable_houses = int(input("How many houses are avaliable to purchase: "))
        avaliable_hotels = int(input("How many hotels are avaliable to purchase:"))

        if cash >= 200:
            can_purchase = calculate_purchasable_amount(cash)
            print(f"The total number of houses or hotels you can buy is {can_purchase:.0f}")
            if avaliable_houses >=1 or avaliable_hotels >= 1:
                action = int(input("What would you like to do? (1: buy house 2: buy hotel 3: swap houses)"))
                if action == 1:
                    purchased, avaliable_houses, pe, nc, pa = buy_house(can_purchase, avaliable_houses, pe, nc, pa)
                elif action == 2:
                    if pe == 4 or nc == 4 or pa == 4:
                        buy_hotel()
                else:
                    swap_houses()
            else:
                print("There aren't enough avaliable houses or hotels")
        else:
            print("You dont have enough cash to purchase anything.")
    else:
        print("You do not own all of the properties on green, you can't build houses here.")