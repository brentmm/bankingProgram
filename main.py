#text files
userData = ""
transData = "transactionData.txt"
loginData = "loginData.txt"

#creating defult files if needed
def defaultFiles(aFile):
    try:
        f = open(aFile)
        f.close()
    except FileNotFoundError:
        f = open(aFile, 'x')
        f.close()
defaultFiles(transData)
defaultFiles(loginData)

#lists
listFile = []
transList = []
userList = []
loginList = []

import datetime
transTime = datetime.datetime.now()
#so transaction dates can be tracked


#removes \n so the text file is organized in a list
def peeling(dataFile):
    aList = []
    user = open(dataFile, 'r')
    all_lines = user.readlines()
    for i in all_lines:
        aList.append(i.replace("\n", ""))
    user.close()
    return aList


#adds \n into the lists so the text file is organized and each index is on its own line
def de_peeling(listFile):
    aList = []
    for i in listFile:
        aList.append("\n" + str(i))
    return aList


#closes a file and saves information to text file
def closing(dataFile, listFile):
    user = open(dataFile, 'w')
    for i in listFile:
        user.write(str(i))
    user.close()


#function to deposit
def deposit(userList, time, transList):
    amountAdded = int(input("What amount are you depositing?: $"))
    print("")
    userList.insert(0, int(userList.pop(0)) + amountAdded)
    transList.append(
        str(time.strftime("%x" + " %X")) + " " + str(accountUser) +
        " Deposited $" + str(amountAdded))
    print("$" + str(amountAdded) + " has been added to your " + '''account''')
    return userList


#function to withdrawl
def withdrawl(userList, time, transList):
    amountSubtracted = int(input("What amount are you withdrawing?: $"))
    if amountSubtracted > int(userList[0]):
        print("Insufficient Funds")
        print("")
    elif amountSubtracted <= int(userList[0]):
        print("")
        userList.insert(0, int(userList.pop(0)) - amountSubtracted)
        transList.append(
            str(time.strftime("%x" + " %X")) + " " + str(accountUser) +
            " Withdrawl $" + str(amountSubtracted))
        print("$" + str(amountSubtracted) +
              " has been removed from your account.")
    return userList


#function to transfer money
def transfer(userList, time, transList, loginList):
    print("")
    transferAccount = input(
        "What account are you transfering to?: ").capitalize()
    print("")
    if transferAccount in loginList:
        transferAmount = int(input("What amount are you transfering?: "))
        print("")
        if transferAmount > int(userList[0]):
            print("Insufficient Funds")
            print("")
        elif transferAmount <= int(userList[0]):
            transConfirm = input("You are transfering $" +
                                 str(transferAmount) + " from " +
                                 str(accountUser) + " to " + transferAccount +
                                 " (yes or no): ").lower()
            print("")
            if transConfirm == ("yes"):
                userList.insert(0, int(userList.pop(0)) - transferAmount)
                transList.append(
                    str(time.strftime("%x" + " %X")) + " Transfered $" +
                    str(transferAmount) + " from " + str(accountUser) +
                    " to " + str(transferAccount))
                print("$" + str(transferAmount) + " has been transfered to " +
                      str(transferAccount))
            else:
                print("TRANSACTION CANCELLED")
    else:
        print("That account does not exist.")

    return userList


#function to quit program
def quit(choice):
    print("")
    print(
        "Thanks for choosing Martin Banking for all your banking needs. Have a splendid day!"
    )


#intro
print("Welcome to Martin Banking Program.")
print("")
userAccount = input("Are you a already existing user? (Yes or No): ").lower()
print("")
while userAccount != "yes" and userAccount != "no":
    userAccount = input("Do you have an account?(Yes or No) ").lower()

transList = peeling(transData)
if len(transList) > 0:
    if transList[0] == "":
        transList.pop(0)

loginList = peeling(loginData)
if len(loginList) > 0:
    if loginList[0] == "":
        loginList.pop(0)

credentials = False
while credentials == False:
    #Login
    if userAccount == ("no"):
        print("Lets setup an account.")
        accountUser = input("Create a username: ").capitalize()
        while accountUser in loginList:
            print("Sorry, " + accountUser +
                  " unavailable. Please chose another username.")
            accountUser = input("Create a username: ").capitalize()
        loginList.append(accountUser)
        accountPass = input("Create a password: ")
        loginList.append(accountPass)
        userOne = open(accountUser + '.txt', 'x')
        userOne.close()
        listFile.append("100")
        userData = accountUser + ".txt"
        credentials = True

    elif userAccount == ("yes"):
        print("Please Enter Your Login Credentials")
        accountUser = input("Username: ").capitalize()
        accountPass = input("Password: ")
        if accountUser in loginList:
            if accountPass == loginList[loginList.index(accountUser) + 1]:
                print("")
                print("Welcome back, " + accountUser)
                credentials = True
                userData = accountUser + ".txt"
                listFile = peeling(userData)
            else:
                print("")
                print("You have entered an invalid password.")
                print("")
        else:
            print("")
            print("Account not found.")
            print()
            credentials = False

if len(listFile) > 0:
    if listFile[0] == "":
        listFile.pop(0)

print("")
print("This is your accounts main menu. From here you can: ")
print("")
print(
    " (1) Deposit \n (2) Withdrawl \n (3) Transfer \n (4) Total Balance \n (5) Quit Progam *Always remember to quit our program to save your data*"
)
print("")
action = "no"
while action == "no":
    #asking user what they want to do
    choice = input("What action would you like to perform?: ")
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        print("")
        print("Invaild action.")
        print("")
        print(
            " (1) Deposit \n (2) Withdrawl \n (3) Transfer \n (4) Total Balance \n (5) Quit Progam"
        )
        print("")
        choice = input("What action would you like to perform? (Select a #) ")
        print("")

    #checking users input and steps into required function function
    if choice == ("1"):
        listFile = deposit(listFile, transTime, transList)
        print("Your total account balance is: $" + str(listFile[0]))
        print("")
    elif choice == ("2"):
        listFile = withdrawl(listFile, transTime, transList)
        print("Your total account balance is: $" + str(listFile[0]))
        print("")
    elif choice == ("3"):
        listFile = transfer(listFile, transTime, transList, loginList)
        print("")
        print("Your total account balance is: $" + str(listFile[0]))
        print("")
    elif choice == ("4"):
        print("Your total account balance is: $" + str(listFile[0]))
        print("")
    elif choice == ("5"):
        print("")
        print("Your total account balance is: $" + str(listFile[0]))
        print("")
        action = input("Would you like to quit? (yes or no): ").lower()
        if action == ("yes"):
            listFile = de_peeling(listFile)
            transList = de_peeling(transList)
            loginList = de_peeling(loginList)
            closing(userData, listFile)
            closing(transData, transList)
            closing(loginData, loginList)
            quit(action)
            print("")
            choice = "Brent"
        if action == ("no"):
            print("")
    else:
        choice = input("What action would you like to perform? (Select a #) ")

    #asking user what they wanna do if choice was not valid
    while choice != "Brent" and choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        choice = input("What action would you like to perform? (Select a #) ")
