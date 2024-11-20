#Python

# 1. Name:
#      Jaxon Powell
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program will sort the contents of a list in alphabetical order. 
# 4. What was the hardest part? Be as specific as possible.
#      I think that this assignment was very easy for me. There wasn't much confusion about the algorithm or how it is meant to work
#      The hardest part for me was figuring out how to get each letter and determine if it was in order
#      I solved this by having a for loop inside a for loop.
# 5. How long did it take for you to complete the assignment?
#      This program took me an hour and 45 minutes to complete.

import json

def alphabetical_sort(sorted_list):

    #This function sorts into alphabetical order.
    #Returns the sorted list
    assert isinstance(sorted_list, list), "Input must be a list."

    for i in range(len(sorted_list) -1, 0, -1):
        end_value = sorted_list[i]

        for j in range(i):
            if sorted_list[j] > end_value:
                sorted_list[j], end_value = end_value, sorted_list[j]

        sorted_list[i] = end_value

    return sorted_list


def main():

    file_name = input("What is the name of the file to sort: ")

    with open (file_name, "r") as file:
        json_data = file.read()
        data = json.loads(json_data)

        items = []

        for i in data:
            items.extend(data[i])
    
    assert isinstance(items, list), "The data must be a list."

    for item in items:

        print(f"    {item}")
    

    sorted_list = alphabetical_sort(items)

    assert sorted_list == sorted(sorted_list), "The list is not properly sorted"

    print("\n\nSorted list \n")

    for sorted_item in sorted_list:

        print(f"    {sorted_item}")


main()