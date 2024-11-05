#Python

# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json

def alphabetical_sort(sorted_list):

    #This function sorts into alphabetical order.
    #Returns the sorted list

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

    print(items)
    print("")

    sorted_list = alphabetical_sort(items)

    print(sorted_list)


main()