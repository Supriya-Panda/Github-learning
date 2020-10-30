# import csv
# with open('database.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
# file_object = open('sample.txt', 'a')
database = {
    'supriya': {
        'name': 'Supi',
        'age': 24,
        'email': 'supi123@gmail.com',
        'password': 'red123',
        'amount': 20000,
    },
    'monalisa': {
        'name': 'Mona',
        'age': 25,
        'email': 'mona123@gmail.com',
        'password': 'red456',
        'amount': 10000,
    },
    'sonalisa': {
        'name': 'Sona',
        'age': 23,
        'email': 'sona123@gmail.com',
        'password': 'red46',
        'amount': 1000,
    }
}


def showAccountDetails(userDetails):
    # print(userDetails)
    count = 0
    print("welcome ", userDetails["name"])
    while count == 0:
        print("1 : CheckBalance \n2 : WithdrawlBalance \n3 : DepositBalance \n4 : Change Password \n5 : LogOut")
        choice1 = (input("enter your choice:"))
        if choice1 == "1":
            print("your account balance is", userDetails["amount"])
            # showAccountDetails(userDetails)
        elif choice1 == "2":
            withdrawlBalance(userDetails)
        elif choice1 == "3":
            depositBalance(userDetails)
        elif choice1 == "4":
            changePassword(userDetails)
        elif choice1 == "5":
            print("logout succeesfully")
            count = 1
            loginAccount()
        else:
            print("invalid")


def changePassword(userDetails):
    newpassword = input("Enter a newpassword:")
    userDetails["password"] = newpassword
    print("Your password has been successfully updated.")


def withdrawlBalance(userDetails):
    balance = int(input("enter withdrawl balance :"))
    if balance < userDetails["amount"]:
        totalbalance = userDetails["amount"] - balance
        print("Transaction Successfull.Your Balance is", totalbalance)
        userDetails["amount"] = totalbalance
        # print(userDetails["amount"])
        # print(database)
    else:
        print("Insufficient Balance")
    # showAccountDetails(userDetails)


def depositBalance(userDetails):
    balance1 = int(input("enter  deposit balance :"))
    totalamount = userDetails["amount"] + balance1
    print("Transaction Successfull.Your Balance is", totalamount)
    userDetails["amount"] = totalamount
    # print(userDetails["amount"])
    # print(database)
    # showAccountDetails(userDetails)


def accountDetails():
    userid = input("enter userid :")
    if userid in database:
        password = input("enter your password:")
        if (database[userid]["password"]) == password:
            showAccountDetails(database[userid])
        else:
            print("please enter correct password")
            print("1 : Forgot Password \n2 : Exit")
            choose = int(input("Enter your choice:"))
            if choose == 1:
                changePassword()
                loginAccount()
            else:
                print("Exit")
    else:
        print("please enter correct userid")


def signUpDetails():
    check = 0
    while check == 0:
        # for key, value in database.items():
        userid = (input("Enter your id:"))
        if userid in database:
            print("userid is already exist")
            check = 0
        else:
            check = 1
            username = input("Enter your name:")
            userage = int(input("Enter your age:"))
            usermail = input("Enter your mailid:")
            userpassword = input("Enter your password:")
            useramount = int(input("Enter your balance:"))
            print("New user successfully added")
            database[userid] = {"name": username, "age": userage, "email": usermail, "password": userpassword,
                                "amount": useramount}
            print(database)
            loginAccount()


def loginAccount():
    print("welcome to our bank account")
    print("1 : SignIn \n2 : SignUp \n3 :  Exit")
    choice = input("enter your choice:")
    # choose=print(input("create a new account:"))
    if choice == "1":
        accountDetails()
    elif choice == "2":
        signUpDetails()
    elif choice == "3":
        print("Thank you for banking with us...")
    else:
        print("invalid")


loginAccount()
