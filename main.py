# use text file to storge the user proflie
# the test file use number to rang them
import random

userList = ""

def user(usercode):
    with open(f"{usercode}.txt", "w") as user:
	    user = user.write(f"user_{usercode}")

def menuLogin():
    global userList
    print("Pls login to play:")
    userList = ""
    with open("user.txt", "r") as user_file:
        userList = user_file.readlines()

    userList = [i.replace('\n','') for i in userList]
    for index, item in enumerate(userList, 1):
        print(f"{index} [{item}]")

def menu():
    print("Do you have an acount?")
    print("1[Login]")
    print("1[Signup]")
    userinput = ""
    while not userinput == 1 or userinput == 2:
        userinput = input()
        try:
            userinput = int(userinput)
        except ValueError:
            print("Please enter a number")
    if userinput == 1:
        menuLogin()



menu()  


