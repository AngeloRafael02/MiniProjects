# Point-of-Sales System
# Made by Angelo Rafael Recio, CPE2A
# Student ID: 2020251

def login():
    """
    This function for taking and storing student data into a dictionary
    """
    while True:
        try:
            StudentName_251 = str(input("Enter your Name: "))
            StudentID_251  = int(input("Enter your Student ID: "))
            Year_251  = str(input("Enter your Year: "))
            Course_251  = str(input("Enter your Course: "))
            Section_251  = str(input("Enter your Section: "))
            break
        except Exception as error:
            print(error)

    global credentials
    credentials = {
        "StudentName" : StudentName_251 ,
        "StudentID": StudentID_251 ,
        "Year" : Year_251 ,
        "Course" : Course_251 ,
        "Section" : Section_251 ,
        "Budget" : float(150.00)
    }
    return credentials


class Order:
    def __init__(self, price_251 ,inventory_251 ):
        """This Constructor function is used to create the Objects and declare its methods and attributes"""
        self.price = float(price_251) 
        self.inventory = inventory_251 
    
    def purchase(self,wallet_251):
        """This method is called when an Object is to be purchased"""
        strWallet_251  = str(wallet_251 )
        worth_251  = str(self.price)
        stock_251  = str(self.inventory)
        print("\nWallet: P" + strWallet_251 )
        print("Price: P" + worth_251 )
        print("Available: "+ stock_251 )
        try:
            confirm = str(input("Confirm Purchase? y/n "))
            if confirm.lower() == 'y':
                if self.inventory <= 0:
                    print("\nSorry, we ran out of stock")
                    print("Transaction Cancelled\n")
                elif self.inventory > 0:
                    if (wallet_251 - self.price) < 0:
                        print("\nSorry, Wallet Amount not enough")
                        print("Transaction Cancelled\n")
                    else:
                        self.inventory -= 1
                        credentials["Budget"] = float(wallet_251)  - float(self.price)
                        change_251 = str(credentials["Budget"])
                        print("Transaction Complete.")
                        print("Wallet: P" + change_251 + "\n" )
                        return change_251 
            elif confirm.lower() == 'n':
                print("Transaction Cancelled")
                print("Wallet: P" + strWallet_251  + "\n")
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
    This is a program made to help students to order their food and drinks without human interaction.
    Type 'Profile' to access User Information. | Type 'Quit' to exit program.
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
    Food_251 = str(input("Please Input what you like: "))
    try:
        if Food_251.lower() == "soda":
            Soda.purchase(wallet)           
        elif Food_251.lower() == "bottled water" or Food_251.lower() == "bottledwater":
            BottleWater.purchase(wallet)
        elif Food_251.lower() == "coffee":
            Coffee.purchase(wallet)
        elif Food_251.lower() == "tea":
            Tea.purchase(wallet)
        elif Food_251.lower() == "bread":
            Bread.purchase(wallet)
        elif Food_251.lower() == "apple":
            Apple.purchase(wallet)
        elif Food_251.lower() == "banana":
            Banana.purchase(wallet)
        elif Food_251.lower() == "oranges":
            Oranges.purchase(wallet)
        elif Food_251.lower() == "tapsilog":
            Tapsilog.purchase(wallet)
        elif Food_251.lower() == "porksilog":
            Porksilog.purchase(wallet)
        elif Food_251.lower() == "profile":
            print("\n")
            print("User Information:")
            for key,value in credentials.items():
                print("> " + key + " - " + str(value))
        elif Food_251.lower() == "quit":
            return 1
    except Exception as error:
            print(error)
    finally:
        print("Ending Program...")

def main():
    """This is the main function and the main entry point and used to structure the other 
        functions as well as to be called to start the program"""
    login()
    while True:
        if display(credentials["Budget"],credentials["StudentName"]) == 1:
            break
    print("\nThanks you for using the Program!")

main()