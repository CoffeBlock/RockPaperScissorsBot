# use text file to storge the user proflie
# the test file use number to rang them
import random

userList = ""

def user(usercode):
    with open(f"{usercode}.txt", "w") as user:
	    user = user.write(f"user_{usercode}")

def menuLogin():
    print("Pls login to play:")
    userList = [i.replace('\n','') for i in userList]
    for index, item in enumerate(userList, 1):
        print(f"{index} [{item}]")

def menuSignup():
    wait = True
    global userList
    while wait == True:
        userinput = input()
        if userList.count(userinput) == 0:
            with open("user.txt", "a") as user_file:
                userList = user_file.write(f"\n{userinput}")
            user(userinput)

            

def menu():
    print("Do you have an acount?")
    print("1[Login]")
    print("2[Signup]")
    userinput = ""
    wait = True
    while wait == True:
        userinput = input()
        try:
            userinput = int(userinput)
            wait = False
        except ValueError:
            print("Please enter a number")
        
    if userinput == 1:
        menuLogin()
    elif userinput == 2:
        menuSignup()

# 1 = rock
# 2 = paper
# 3 = scissors



userList = ""
with open("user.txt", "r") as user_file:
    userList = user_file.readlines()

menu()



