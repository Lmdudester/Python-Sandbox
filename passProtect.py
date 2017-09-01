import os

#Creates a new account under a given service
def addAccount(fullpath):
    newFile = open(fullpath, "w")

    resp = input("Email: (Leave blank if none) ")
    #ENCRYPT Email
    newFile.write(resp + "\n")

    resp = input("Username: (Leave blank if none) ")
    #ENCRYPT Username
    newFile.write(resp + "\n")

    resp = input("Password: ")
    #ENCRYPT Password
    newFile.write(resp + "\n")

#Enter a service to get information for
def getService(incompletePath):
    while True:
        service = input("Enter the name of the service: ")
        path = incompletePath + "\\" + service.lower()

        if not os.path.isdir(path) or incompletePath + "\\" == path:
            print("Not an available service.")

            #Allow for Service Addition
            resp = input("Would you like to add this service? (Y/N) ")
            if resp.lower() == 'y':
                os.makedirs(incompletePath + "\\" + service.lower())
                print("Service Added.")

            elif resp.lower() != 'n':
                print("Invalid response...")

            continue
        else:
            print("Service found.")
            return path

#Enter an Account to get information for
def accessAcct(path):
    while True:
        acct = input("Enter the account name: ")
        fullpath = path + "\\" + acct.lower() + ".txt"

        if not os.path.isfile(fullpath):
            print("Not an available account.")

            #Allow for Account Addition
            resp = input("Would you like to add an account? (Y/N) ")
            if resp.lower() == 'y':
                 addAccount(fullpath)
                 print("File Created.")

            elif resp.lower() != 'n':
                print("Invalid response...")

            continue
        else:
            print("Account found.")
            return fullpath

infoDict = {"email":"", "username":"", "password":""}

#Preset Path
incompletePath = os.path.abspath(".\Passwords")

#Determine Service and Account
path = getService(incompletePath)
path = accessAcct(path);

#Open file and obtains Encrypted data
passFile = open(path)
infoDict["email"] = passFile.readline()[:-1]
infoDict["username"] = passFile.readline()[:-1]
infoDict["password"] = passFile.readline()[:-1]

#Ask for info type
while True:
    decision = input("What information would you like to access? (Q to quit)\n(E - email, U - Username, P - Password) ")

    if decision.lower() == 'e': #Email
        #DECRYPT HERE
        print("\n" + infoDict["email"] + "\n")

    elif decision.lower() == 'u': #Username
        #DECRYPT HERE
        print("\n" + infoDict["username"] + "\n")

    elif decision.lower() == 'p': #Password
        #DECRYPT HERE
        print("\n" + infoDict["password"] + "\n")

    elif decision.lower() == 'q': #Quit
        print("Exiting...")
        break

    else:
        print("\nNot an option!\n")
