# Point-of-Sales System
# Made by Angelo Rafael Recio, CPE2A
# Student ID: 2020251
# NOTE to self: 
# - rewrite "newReceipt.html" file address when uploading to other IDEs/Repositories
# - include empty "newReceipt.html" file in uploading. or not if it will write itself anyways

def login():
    """
    This function for taking and storing student data into a dictionary
    """
    while True:
        try:
            StudentName_251 = str(input("Enter your Name: "))
            StudentID_251 = str(input("Enter your Student ID: "))
            Year_251 = str(input("Enter your Year: "))
            Course_251 = str(input("Enter your Course: "))
            Section_251 = str(input("Enter your Section: "))
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

        "defaultInitialMoney": int(150),
        "TransactionTotal": float(0),
        "Budget" : float(150.00)
    }
    return credentials

def welcomeReceipt(shopName):
    """Prints first at the receipt, after credentials have been filled with data
    Also sets up styles and CSS"""
    try:
        f = open('MiniProjects/PythonPOS/HtmlReceipt.html', 'w') #NOTE: Do replace file address when migrating to other files
        f.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">')
        f.write('<style> \
                    body{  background-image:url(https://i.redd.it/uuqjrkfblih61.jpg); height: 100%; background-position: center; background-size: cover;}\n \
                    p{ color:white; font-family: Arial; font-size:25px; text-align:center;}\n\
                    div{ display:flex; justify-content:center;}    \
                    .btn{ color:white; margin:auto; margin-left:2px; margin-right:2px; }    \n\
                    span{ font-size: 120%; }\n    \
                </style><br>\n')
        f.write('\
                <script>\n \
                    function refresh(){ window.location.reload() }\n \
                    function displayCredits(){ alert("Made By: Angelo Rafael F. Recio :)"); }\n \
                    function showCredentials(){ alert("Name: '+credentials["StudentName"] + ' | StudentID: ' + credentials["StudentID"] + ' | Year: ' + credentials["Year"] + ' | Course: ' + credentials["Course"]+ ' | Section: ' + credentials["Section"] +'"); }\n \
                </script>\n')
        f.write("<div>\
                    <div class='buttonArr'>\
                        <button type='button' class='btn btn-info' onclick='refresh()'> Update / Refresh Page </button>\n \
                        <button  type='button' class='btn btn-info' onclick='displayCredits()'> Credits </button>\n \
                        <button  type='button' class='btn btn-info' onclick='showCredentials()'> Show Current User </button>\n \
                    </div>\
                </div>"\
                + '<p><span>' + shopName + "</span><br>\n" \
                + "User: " + credentials["StudentName"] + "<br>\n" \
                + "-------------------------------" + "</p>\n")
    except Exception as error:
        print(error)  
        f.close()
    finally:
        f.close()

def HTMLIndent():
    return "'\n'"        

def endingReceipt(shopName):
    """Prints at the End of the Receipt After the Transactions is Finished"""
    try:
        f = open('MiniProjects/PythonPOS/HtmlReceipt.html', 'a')
        f.write("<p>-------------------------------" + "<br>" + "\n" \
            + "Thank You for Purchasing in" + "<br>" + "\n"\
            + shopName + "!</p>" + "\n")
        f.close()
    finally:
        f.close()

class Order:
    def __init__(self,name_251, price_251 ,inventory_251 ):
        """This Constructor function is used to create the Objects and declare its methods and attributes"""
        self.name:str = str(name_251)
        self.price:float = float(price_251) 
        self.inventory:int = int(inventory_251) 

    @staticmethod
    def indentMaker(name):
        if len(name) == 4 or len(name) == 5:
            return "\t\t\t\t\t" + "&nbsp;"
        elif len(name) == 6 or len(name) == 7 or len(name) == 8 or len(name) == 9:
            return "\t\t\t\t" + "&nbsp;"
        elif len(name) > 9:
            return "\t\t\t" + "&nbsp;"
    
    def purchase(self,wallet_251):
        """This method is called when an Object is to be purchased"""
        strWallet_251  = str(wallet_251 )
        worth_251  = str(self.price)
        stock_251  = str(self.inventory)
        print("\nWallet: P" + strWallet_251[0:5] )
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
                        self.inventory -= 1 # inventory decrease
                        credentials["Budget"] = float(wallet_251)  - float(self.price) #budget changed
                        change_251 = str(credentials["Budget"])
                        credentials["TransactionTotal"] += self.price
                        f = open('MiniProjects/PythonPOS/HtmlReceipt.html', 'a') #purchase appended
                        f.write("<p> > "+ self.name + self.indentMaker(self.name) + "P" + worth_251  + "</p>" + "\n")
                        f.close()
                        print("Transaction Complete.")
                        print("Wallet: P" + change_251 + "\n" )
                        return change_251 
            elif confirm.lower() == 'n':
                print("Transaction Cancelled")
                print("Wallet: P" + strWallet_251  + "\n")
        except Exception as error:
            print(error)        
            

#Objects Made by the Constructor
Soda = Order("Soda", 29.95, 4)
BottleWater = Order("Bottled Water",20, 4)
Coffee = Order("Coffee", 50, 2) 
Tea = Order("Tea", 35, 2)
Bread = Order("Bread", 15, 1)
Apple = Order("Apple",20.50, 5)
Banana = Order("Banana", 15, 5)
Oranges = Order("Orange", 25.10, 3)
Tapsilog = Order("Tapsilog",80.99, 5)
Porksilog = Order("Porksilog",80.99, 4)

def display(wallet):
    """
                                WELCOME TO THE PROGRAM!
    This is a program made to help students to order their food and drinks without human interaction.
    Type 'Profile' to access User Information. | Type 'Quit'/'End' to Exit program/End transaction.
    MENU
        DRINKS:                       SNACKS:                 MEALS:
        > Soda ----------- P29.95     > Bread ---- P15.00     > Tapsilog ---- P80.99
        > Bottled Water -- P20.00     > Apple ---- P20.50     > Porksilog --- P80.99
        > Coffee --------- P50.00     > Banana --- P15.00
        > Tea ------------ P35.50     > Oranges -- 25.10
    """
    strWallet = str(wallet)
    print(display.__doc__)  
    print("Welcome, " + credentials["StudentName"])
    print("Wallet: P" + strWallet[0:5])
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
        elif Food_251.lower() == "quit" or Food_251.lower() == "end":
            try:
                f = open('MiniProjects/PythonPOS/HtmlReceipt.html', 'a')
                f.write("<p>-------------------------------" + "</p>" + "\n"\
                    + "<p>Total: \t\t\t\t\tP" + str(credentials["TransactionTotal"]) +  "</p>\n"\
                    + "<p>Payment: \t\t\t\tP" + str(credentials["defaultInitialMoney"]) +  "</p>\n"\
                    + "<p>Change: \t\t\t\tP" + str(credentials["Budget"])[0:5] +  "</p>\n")
                f.close()
            except Exception as error:
                print(error)  
                f.close()
            finally:
                f.close()
            return 1
    except Exception as error:
            print(error)
    finally:
        print("Ending Program...")

def main():
    """This is the main function and the main entry point and used to structure the other 
        functions as well as to be called to start the program"""
    login()
    welcomeReceipt("Wangshu Inn")
    while True:
        if display(credentials["Budget"]) == 1:
            break
    endingReceipt("Wangshu Inn")
    print("\nThanks you for using the Program!")

main()