# Point-of-Sales System
# Made by Angelo Rafael Recio

import Menu

def display(wallet):
    """
                                WELCOME TO THE PROGRAM!
    This is a program made to help students to order their food and drink without human interaction
    MENU
        DRINKS:                       SNACKS:                 MEALS:
        > Soda ----------- P29.95     > Bread ---- P15.00     > Tapsilog ---- P80.99
        > Bottled Water -- P20.00     > Apple ---- P20.50     > Porksilog --- P80.99
        > Coffee --------- P50.00     > Banana --- P15.00
        > Tea ------------ P35.50     > Oranges -- 25.10
    """
    while True:
        print(display.__doc__)
        strWallet = str(wallet)
        print("Wallet: " + strWallet)
        Food = str(input("Please Input what you like: "))
        #SODA
        if Food.lower() == "soda":
            print("Wallet: " + strWallet)
            worth = str(Menu.Soda.price)
            stock = str(Menu.Soda.inventory)
            print("Price: " + worth)
            print("Available: "+ stock)
            try:
                confirm = str(input("Confirm Purchase? y/n "))
                if confirm.lower() == 'y':
                    if Menu.Soda.inventory <= 0:
                        print("Sorry we ran out of stock")
                    elif Menu.Soda.inventory > 0:
                        if (wallet - Menu.Soda.price) < 0:
                            print("Sorry, Wallet Amount not enough")
                        else:
                            Menu.Soda.inventory -= 1
                            wallet -= Menu.Soda.price
                    print("Wallet: " + strWallet)
                    print("Transaction Complete.\n")
                    display(wallet)
                elif confirm.lower() == 'n':
                    display(wallet)
            except Exception as error:
                print(error)
        #BOTTLED WATER
        if Food.lower() == "bottled water":
            print("Wallet: " + strWallet)
            worth = str(Menu.BottledWater.price)
            stock = str(Menu.BottledWater.inventory)
            print("Price: " + worth)
            print("Available: "+ stock)
            try:
                confirm = str(input("Confirm Purchase? y/n "))
                if confirm.lower() == 'y':
                    if Menu.BottledWater.inventory <= 0:
                        print("Sorry we ran out of stock")
                    elif Menu.BottledWater.inventory > 0:
                        if (wallet - Menu.BottledWater.price) < 0:
                            print("Sorry, Wallet Amount not enough")
                        else:
                            Menu.BottledWater.inventory -= 1
                            wallet -= Menu.BottledWater.price
                    print("Wallet: " + strWallet)
                    print("Transaction Complete.\n")
                    display(wallet)
                elif confirm.lower() == 'n':
                    display(wallet)
            except Exception as error:
                print(error)
        #COFFEE
        if Food.lower() == "coffee":
            print("Wallet: " + strWallet)
            worth = str(Menu.Coffee.price)
            stock = str(Menu.Coffee.inventory)
            print("Price: " + worth)
            print("Available: "+ stock)
            try:
                confirm = str(input("Confirm Purchase? y/n "))
                if confirm.lower() == 'y':
                    if Menu.Coffee.inventory <= 0:
                        print("Sorry we ran out of stock")
                    elif Menu.Coffee.inventory > 0:
                        if (wallet - Menu.Coffee.price) < 0:
                            print("Sorry, Wallet Amount not enough")
                        else:
                            Menu.Coffee.inventory -= 1
                            wallet -= Menu.Coffee.price
                    print("Wallet: " + strWallet)
                    print("Transaction Complete.\n")
                    display(wallet)
                elif confirm.lower() == 'n':
                    display(wallet)
            except Exception as error:
                print(error)
        #TEA
        if Food.lower() == "tea":
            print("Wallet: " + strWallet)
            worth = str(Menu.Tea.price)
            stock = str(Menu.Tea.inventory)
            print("Price: " + worth)
            print("Available: "+ stock)
            try:
                confirm = str(input("Confirm Purchase? y/n "))
                if confirm.lower() == 'y':
                    if Menu.Tea.inventory <= 0:
                        print("Sorry we ran out of stock")
                    elif Menu.Tea.inventory > 0:
                        if (wallet - Menu.Tea.price) < 0:
                            print("Sorry, Wallet Amount not enough")
                        else:
                            Menu.Tea.inventory -= 1
                            wallet -= Menu.Tea.price
                    print("Wallet: " + strWallet)
                    print("Transaction Complete.\n")
                    display(wallet)
                elif confirm.lower() == 'n':
                    display(wallet)
            except Exception as error:
                print(error)
        #BREAD
        if Food.lower() == "bread":
            print("Wallet: " + strWallet)
            worth = str(Menu.Bread.price)
            stock = str(Menu.Bread.inventory)
            print("Price: " + worth)
            print("Available: "+ stock)
            try:
                confirm = str(input("Confirm Purchase? y/n "))
                if confirm.lower() == 'y':
                    if Menu.Bread.inventory <= 0:
                        print("Sorry we ran out of stock")
                    elif Menu.Bread.inventory > 0:
                        if (wallet - Menu.Bread.price) < 0:
                            print("Sorry, Wallet Amount not enough")
                        else:
                            Menu.Bread.inventory -= 1
                            wallet -= Menu.Bread.price
                    print("Wallet: " + strWallet)
                    print("Transaction Complete.\n")
                    display(wallet)
                elif confirm.lower() == 'n':
                    display(wallet)
            except Exception as error:
                print(error)
        #APPLE
        if Food.lower() == "apple":
            print("Wallet: " + strWallet)
            worth = str(Menu.Apple .price)
            stock = str(Menu.Apple .inventory)
            print("Price: " + worth)
            print("Available: "+ stock)
            try:
                confirm = str(input("Confirm Purchase? y/n "))
                if confirm.lower() == 'y':
                    if Menu.Apple .inventory <= 0:
                        print("Sorry we ran out of stock")
                    elif Menu.Apple .inventory > 0:
                        if (wallet - Menu.Apple .price) < 0:
                            print("Sorry, Wallet Amount not enough")
                        else:
                            Menu.Apple .inventory -= 1
                            wallet -= Menu.Apple .price
                    print("Wallet: " + strWallet)
                    print("Transaction Complete.\n")
                    display(wallet)
                elif confirm.lower() == 'n':
                    display(wallet)
            except Exception as error:
                print(error)
        #BANANA
        if Food.lower() == "banana":
            print("Wallet: " + strWallet)
            worth = str(Menu.Banana .price)
            stock = str(Menu.Banana .inventory)
            print("Price: " + worth)
            print("Available: "+ stock)
            try:
                confirm = str(input("Confirm Purchase? y/n "))
                if confirm.lower() == 'y':
                    if Menu.Banana .inventory <= 0:
                        print("Sorry we ran out of stock")
                    elif Menu.Banana .inventory > 0:
                        if (wallet - Menu.Banana .price) < 0:
                            print("Sorry, Wallet Amount not enough")
                        else:
                            Menu.Banana .inventory -= 1
                            wallet -= Menu.Banana .price
                    print("Wallet: " + strWallet)
                    print("Transaction Complete.\n")
                    display(wallet)
                elif confirm.lower() == 'n':
                    display(wallet)
            except Exception as error:
                print(error)
        #ORANGES
        if Food.lower() == "oranges":
            print("Wallet: " + strWallet)
            worth = str(Menu.Oranges .price)
            stock = str(Menu.Oranges .inventory)
            print("Price: " + worth)
            print("Available: "+ stock)
            try:
                confirm = str(input("Confirm Purchase? y/n "))
                if confirm.lower() == 'y':
                    if Menu.Oranges .inventory <= 0:
                        print("Sorry we ran out of stock")
                    elif Menu.Oranges .inventory > 0:
                        if (wallet - Menu.Oranges .price) < 0:
                            print("Sorry, Wallet Amount not enough")
                        else:
                            Menu.Oranges .inventory -= 1
                            wallet -= Menu.Oranges .price
                    print("Wallet: " + strWallet)
                    print("Transaction Complete.\n")
                    display(wallet)
                elif confirm.lower() == 'n':
                    display(wallet)
            except Exception as error:
                print(error)
        #TAPSILOG
        if Food.lower() == "tapsilog":
            print("Wallet: " + strWallet)
            worth = str(Menu.Tapsilog .price)
            stock = str(Menu.Tapsilog .inventory)
            print("Price: " + worth)
            print("Available: "+ stock)
            try:
                confirm = str(input("Confirm Purchase? y/n "))
                if confirm.lower() == 'y':
                    if Menu.Tapsilog .inventory <= 0:
                        print("Sorry we ran out of stock")
                    elif Menu.Tapsilog .inventory > 0:
                        if (wallet - Menu.Tapsilog .price) < 0:
                            print("Sorry, Wallet Amount not enough")
                        else:
                            Menu.Tapsilog .inventory -= 1
                            wallet -= Menu.Tapsilog .price
                    print("Wallet: " + strWallet)
                    print("Transaction Complete.\n")
                    display(wallet)
                elif confirm.lower() == 'n':
                    display(wallet)
            except Exception as error:
                print(error)
        #PORKSILOG
        if Food.lower() == "porksilog":
            print("Wallet: " + strWallet)
            worth = str(Menu.Porksilog .price)
            stock = str(Menu.Porksilog .inventory)
            print("Price: " + worth)
            print("Available: "+ stock)
            try:
                confirm = str(input("Confirm Purchase? y/n "))
                if confirm.lower() == 'y':
                    if Menu.Porksilog .inventory <= 0:
                        print("Sorry we ran out of stock")
                    elif Menu.Porksilog .inventory > 0:
                        if (wallet - Menu.Porksilog .price) < 0:
                            print("Sorry, Wallet Amount not enough")
                        else:
                            Menu.Porksilog .inventory -= 1
                            wallet -= Menu.Porksilog .price
                    print("Wallet: " + strWallet)
                    print("Transaction Complete.\n")
                    display(wallet)
                elif confirm.lower() == 'n':
                    display(wallet)
            except Exception as error:
                print(error)

def main():
    import studentData
    wallet = studentData.credentials.get("Budget")
    display(wallet)   

main()