misc={
    "defaultInitialMoney": int(150),
    "TransactionTotal": float(round(0,2)),
    "Budget" : float(round(150.00,2))
}

class Order:
    def __init__(self,name_251, price_251 ,inventory_251 ):
        """This Constructor function is used to create the Objects and declare its methods and attributes"""
        self.name:str = str(name_251)
        self.price:float = float(price_251) 
        self.inventory:int = int(inventory_251) 

    @staticmethod
    def indentMaker(name:str):
        """used to print indents according to the number of letters in the Object's name for HTML. """
        if len(name) == 3:
            return "&emsp;&emsp;&emsp;&emsp;&emsp;" 
        elif len(name) == 4:
            return "&emsp;&emsp;&emsp;&ensp;&nbsp;"
        elif len(name) == 5:
            return "&emsp;&emsp;&emsp;&emsp;"
        elif len(name) == 6:
            return "&emsp;&emsp;&emsp;&ensp;"
        elif len(name) == 7 :
            return "&emsp;&emsp;&emsp;&nbsp;" 
        elif len(name) == 8 :
            return "&emsp;&emsp;&ensp;" 
        elif len(name) == 9:
            return "&emsp;&emsp;&nbsp;" 
        elif len(name) > 9:
            return "&ensp;" 
    
    def purchase(self,wallet_251):
        """This method is called when an Object is to be purchased"""
        strWallet_251:str = str(wallet_251 )
        worth_251:str = str(self.price)
        stock_251:str = str(self.inventory)
        print("\nWallet: P" + strWallet_251[0:5] )
        print("Price: P" + worth_251 )
        print("Available: "+ stock_251 )
        try:
            quantity:int = int(input("How many do you want? "))
            confirm:str = str(input("Confirm Purchase? y/n "))
            if confirm.lower() == 'y':
                if quantity > self.inventory:
                    print("\nSorry, Current stock is not enough")
                    print("Transaction cancelled\n")
                if self.inventory <= 0 or quantity > self.inventory:
                    print("\nSorry, we ran out of stock")
                    print("Transaction Cancelled\n")
                elif self.inventory > 0:
                    if (wallet_251 - self.price*quantity) < 0:
                        print("\nSorry, Wallet Amount not enough")
                        print("Transaction Cancelled\n")
                    else:
                        self.inventory -= quantity # inventory decrease
                        misc["Budget"] = float(wallet_251)  - float(self.price)*quantity #budget changed
                        change_251 = str(misc["Budget"])
                        misc["TransactionTotal"] += self.price*quantity #expenditure increased
                        f = open('MiniProjects/PythonPOS/MultiPageVersion/receipt.html', 'a') #purchase appended
                        f.write("<p> "+ str(quantity) + " - " + self.name + self.indentMaker(self.name) + "P" + str(self.price*quantity)  + "</p>" + "\n")
                        f.close()
                        print("Transaction Complete.")
                        print("Wallet: P" + change_251[0:5] + "\n" )
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

menu = {
    "Soda":Soda,
    "BottleWater":BottleWater,
    "Coffee":Coffee,
    "Tea":Tea,
    "Bread":Bread,
    "Apple":Apple,
    "Banana":Banana,
    "Oranges":Oranges,
    "Tapsilog":Tapsilog,
    "Porksilog":Porksilog
}