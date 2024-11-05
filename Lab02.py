# 1. Name:
'''Jaxon Powell'''
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
'''In this program you will enter a username and password
It will then check to see if that username and password 
are stored in a list containing multiple usernames and passwords'''
# 4. What was the hardest part? Be as specific as possible.
"""The hardest part about this assignment for me was figuring out
how to import the JSON file and to get it to stored into a list. 
I found this difficult because I have never done it before. 
I have worked with .csv and .txt files before but never a JSON file. 
In the end it ended up being a little similar. I had to do a little research
to figure it out. W3 school was helpful in explaining it and how it works.""" 
# 5. How long did it take for you to complete the assignment?
'''This assignment took me 2 hours total to complete'''    

# Was the syntax of Python the hardest part? If so, what part?
'''The hardest part about the syntax for me was figuring out the 
eaisest way to read the JSON file and add it into a list'''
# Was there some aspect of the problem that was particularly difficult to solve?
'''Along with working with the JSON file the hardest part was 
figuring out how to check if both the username and password were correct'''
# Was there an especially difficult bug? If so, how did you resolve it?
'''My program got a little buggy trying to store the usernames and passwords
into a list. I solved this by going to W3schools.com and learning about 
importing and working with JSON files'''
# Was there some difficulty with the instructions or any part of the problem definition?
'''No I wasn't confused at all with any of the instruction or definition'''


import json

# In this function it takes the user input and checks to see
# if there is a username in the list that is the same as the user input
def username_checker(username_attempt, usernames):
    username_found = False
    if username_attempt in usernames:
        username_found = True
    return username_found

# In this function it takes the user input and checks to see
# if there is a pssword in the list that is the same as the user input
def password_checker(password_attempt, passwords):
    password_found = False
    if password_attempt in passwords:
        password_found = True
    return password_found

# Main function 
def main():

    #Opening the json file in read mode
    with open('Lab02.json', 'r') as file:
        json_data = file.read()

    # Converts the JSON file in to a python object such as a list
    data = json.loads(json_data)

    # Converts the username and password components into two separate lists
    usernames = list(data['username']) 
    passwords = list(data['password'])  

    # Asks the user to input a username and a password
    #and stores it in a variable
    username_attempt = input("Enter a username: ")
    password_attempt = input("Enter a password: ")

    #Calls the username_ checker and the password_checker function
    #and passes in the variables to use
    username_found = username_checker(username_attempt, usernames)
    password_found = password_checker(password_attempt, passwords)

    #The checker functions return a boolean variable that this if statement
    #checks to see if they are both true. 
    #If they are both true then it wil, say access has been allowed
    #If none or one of them is false then it will print that 
    #access wasnt granted. 
    if username_found == True and password_found == True:
        print(f"\nYou have been allowed access.")
        print(f"The user name is {username_attempt}")
        print(f"The password is {password_attempt}\n")
    
    else:
        print("You are not authorized to use the system.")


# Running the main function
main()