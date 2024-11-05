#Python

import json

def print_error_message(error):
    print(f"Error: {error}")

def search_list(name, list, i_first, i_last):
    searching_name = name
    found = False
    while i_first <= i_last and found == False:

        i_middle = (i_first + i_last) / 2
        i_middle = int(i_middle)

        if list[i_middle] < name:
            i_first = i_middle + 1
        elif list[i_middle] > name:
            i_last = i_middle - 1
        elif searching_name == name:
            found = True
            return name
        else:
            print("That language is not found")



def main():

    
    try:
        file_name = input("What is the name of the file: ")
        with open(file_name, "r") as file:
            json_data = file.read()
            data = json.loads(json_data)

            languages = []

            for i in data:
                languages.extend(data[i])

        print(languages)
        name = input("What name do you want to look for:")

        i_first = 0
        i_last = len(languages)

        found_name = search_list(name, languages, i_first, i_last)

        if found_name == name:

            print("This is the end of the program, the language was found.")
            print(f"The language was {found_name}")
        else:
            print("That language is not found in this file.")

    except:
        print(f"Please enter the file name again.")


    

main()

