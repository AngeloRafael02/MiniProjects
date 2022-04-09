# Point-of-Sales System
# Made by Angelo Rafael Recio

class Student():
    def __init__(self,name,id,year,course,section,budget):
        self.name = name
        self.id = id
        self.year = year
        self.course = course
        self.section = section
        self.budget = budget

class Order():
    def __init__(self,price,inventory):
        """This Constructor function is used to create the Objects and declare its methods and attributes"""
        self.price = price
        self.inventory = inventory
    
    def purchase(self,wallet):
        """This method is called when an Object is to be purchased"""
        strWallet = str(wallet)
        worth = str(self.price)
        stock = str(self.inventory)
        print("Wallet: P" + strWallet)
        print("Price: P" + worth)
        print("Available: "+ stock)
        try:
            confirm = str(input("Confirm Purchase? y/n "))
            if confirm.lower() == 'y':
                if self.inventory <= 0:
                    print("\nSorry, we ran out of stock")
                    print("Transaction Cancelled")
                elif self.inventory > 0:
                    if (wallet - self.price) < 0:
                        print("\nSorry, Wallet Amount not enough")
                        print("Transaction Cancelled")
                    else:
                        self.inventory -= 1
                        self.budget = wallet - self.price
                        change = str(self.budget)
                        print("Transaction Complete.")
                        print("Wallet: P" + change + "\n" )
                        return change
            elif confirm.lower() == 'n':
                print("Transaction Cancelled")
                print("Wallet: P" + strWallet + "\n")
        except Exception as error:
            print(error)

#Objects Made by the Constructor
Soda = Order(29.95, 4)
BottleWater = Order(20, 4)
Coffee = Order(50, 2)
Tea = Order(35, 2)
Bread = Order(15, 1)
Apple = Order(20.50, 5)
Banana = Order(15, 5)
Oranges = Order(25.10, 3)
Tapsilog = Order(80.99, 5)
Porksilog = Order(80.99, 4)


def display(wallet,name):
    """
                                WELCOME TO THE PROGRAM!
    This is a program made to help students to order their food and drink without human interaction.
    Type 'Quit' to exit program
    MENU
        DRINKS:                       SNACKS:                 MEALS:
        > Soda ----------- P29.95     > Bread ---- P15.00     > Tapsilog ---- P80.99
        > Bottled Water -- P20.00     > Apple ---- P20.50     > Porksilog --- P80.99
        > Coffee --------- P50.00     > Banana --- P15.00
        > Tea ------------ P35.50     > Oranges -- 25.10
    """

    strWallet = str(wallet)
    print(display.__doc__)  
    print("Welcome, " + name)
    print("Wallet: P" + strWallet)
    Food = str(input("Please Input what you like: "))
    try:
        if Food.lower() == "soda":
            Soda.purchase(wallet)           
        elif Food.lower() == "bottled water":
            BottleWater.purchase(wallet)
        elif Food.lower() == "coffee":
            Coffee.purchase(wallet)
        elif Food.lower() == "tea":
            Tea.purchase(wallet)
        elif Food.lower() == "bread":
            Bread.purchase(wallet)
        elif Food.lower() == "apple":
            Apple.purchase(wallet)
        elif Food.lower() == "banana":
            Banana.purchase(wallet)
        elif Food.lower() == "oranges":
            Oranges.purchase(wallet)
        elif Food.lower() == "tapsilog":
            Tapsilog.purchase(wallet)
        elif Food.lower() == "porksilog":
            Porksilog.purchase(wallet)
        elif Food.lower() == "quit":
            return 1
    except Exception as error:
            print(error)

def main():
    """This is the main function used to structure the other functions as well as to be called to start the program"""
    user = Student(\
        name = str(input("Enter name: ")),\
        id = int(input("Enter ID: ")),\
        year = str(input("Enter year: ")),\
        course = str(input("Enter course: ")),\
        section = str(input("Enter Section: ")),\
        budget = 150)
    while True:
        if display(user.budget,user.name) == 1:
            break
    print("Thanks you for using the Program!")

main()

##TO BE CONTINUED