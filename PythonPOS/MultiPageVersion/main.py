# Point-of-Sales System (Multi-File Version)
# Made by Angelo Rafael Recio, CPE2A
# Student ID: 2020251
# NOTE to self: 
# - rewrite "newReceipt.html"'s file address when uploading to other IDEs/Repositories
# - include empty "newReceipt.html" file in uploading, or not if it will write itself anyways

from menuFile import menu, misc
 
def main()->None:
    global studentdata
    import studentdata
    RestaurantName:str = "Wangshu Inn"
    welcomeReceipt(RestaurantName)
    while True:
        if display(misc["Budget"]) == 1:
            break
    endingReceipt(RestaurantName)
    print("Thank you for using the program!")

def welcomeReceipt(shopName:str)->None:
    """Prints first at the receipt, after credentials have been filled with user data.
    Also sets up styles with CSS, and additional scripts with JavaScript"""
    try:
        f = open('MiniProjects/PythonPOS/MultiPageVersion/receipt.html', 'w') #NOTE: Do replace file address when migrating to other files
        f.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"> \n ')
        f.write('<style> \
                    body{  background-image:url(https://i.redd.it/uuqjrkfblih61.jpg); height: 100%; background-position: center; background-size: cover;}\n \
                    p{background-image: url(https://wallpaperaccess.com/full/2796640.jpg); width: 200px; color:black; font-family:"Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif; font-size:18px;  text-align:center; margin-bottom:0px; margin-left: 43%; }\n \
                    div{ display:flex; justify-content:center;} \n   \
                    .btn{ color:white; margin:auto; margin-left:2px; margin-right:2px; }    \n\
                    span{ font-size: 120%; }\n    \
                </style><br>\n')
        f.write('\
                <script>\n \
                    function refresh(){ window.location.reload() }\n \
                    function displayCredits(){ alert("Made By: Angelo Rafael F. Recio :)"); }\n \
                    function showCredentials(){ \
                        alert("Name: '+ studentdata.USER.name \
                         + ' | StudentID: ' + studentdata.USER.id \
                         + ' | Year: ' + studentdata.USER.year \
                         + ' | Course: ' + studentdata.USER.course \
                         + ' | Section: ' + studentdata.USER.section +'"); }\n \
                </script>\n')
        f.write("<div>\
                    <div class='buttonArr'>\
                        <button type='button' class='btn btn-info' onclick='refresh()'> Update / Refresh Page </button>\n \
                        <button  type='button' class='btn btn-info' onclick='displayCredits()'> Credits </button>\n \
                        <button  type='button' class='btn btn-info' onclick='showCredentials()'> Show Current User </button>\n \
                    </div>\
                </div>"\
                + '\n<br><p>Welcome to <br> <span>' + shopName + "</span><br>\n" \
                + "User: " + studentdata.USER.name + "<br>\n" \
                + "ID: " + studentdata.USER.id + "<br>\n" \
                + "-------------------------------<br>\n" \
                + "#&emsp;Name&emsp;&emsp;&emsp;&ensp;Price</p>\n")
    except Exception as error:
        print(error)  
        f.close()
    finally:
        f.close() 

def display(wallet:float or int):
    """
                                WELCOME TO THE PROGRAM!
     This is a program made to help students to order their food and drinks without human interaction.
    Type 'Profile' to access User Information. | Type 'Quit'/'End' to Exit program and End transaction.
    MENU
        DRINKS:                       SNACKS:                 MEALS:
        > Soda ----------- P29.95     > Bread ---- P15.00     > Tapsilog ---- P80.99
        > Bottled Water -- P20.00     > Apple ---- P20.50     > Porksilog --- P80.99
        > Coffee --------- P50.00     > Banana --- P15.00
        > Tea ------------ P35.50     > Oranges -- 25.10
    """
    strWallet:str = str(wallet)
    print(display.__doc__)  
    print("Welcome, " + studentdata.USER.name)
    print("Wallet: P" + strWallet[0:5])
    Food_251:str = str(input("Please Input what you like: "))
    try:
        if Food_251.lower() == "soda":
            menu["Soda"].purchase(wallet)           
        elif Food_251.lower() == "bottled water" or Food_251.lower() == "bottledwater":
            menu["BottleWater"].purchase(wallet)
        elif Food_251.lower() == "coffee":
            menu["Coffee"].purchase(wallet)
        elif Food_251.lower() == "tea":
            menu["Tea"].purchase(wallet)
        elif Food_251.lower() == "bread":
            menu["Bread"].purchase(wallet)
        elif Food_251.lower() == "apple":
            menu["Apple"].purchase(wallet)
        elif Food_251.lower() == "banana":
            menu["Banana"].purchase(wallet)
        elif Food_251.lower() == "oranges":
            menu["Oranges"].purchase(wallet)
        elif Food_251.lower() == "tapsilog":
            menu["Tapsilog"].purchase(wallet)
        elif Food_251.lower() == "porksilog":
            menu["Porksilog"].purchase(wallet)
        elif Food_251.lower() == "profile":
            print("\n")
            print("User Information:")
            for key,value in studentdata.iterable.items():
                print("> " + key + " - " + str(value))
        elif Food_251.lower() == "quit" or Food_251.lower() == "end":
            try:
                f = open('MiniProjects/PythonPOS/MultiPageVersion/receipt.html', 'a')
                f.write("<p>-------------------------------" + "</p>" + "\n"\
                    + "<p>Total:&emsp;&emsp;&emsp;&emsp;&ensp;&nbsp;P" + str(round(misc["TransactionTotal"],2)) +  "</p>\n"\
                    + "<p>Payment:&emsp;&emsp;&emsp;&emsp;P" + str(round(misc["defaultInitialMoney"],2)) +  "</p>\n"\
                    + "<p>Change:&emsp;&emsp;&emsp;&emsp;&nbsp;P" + str(round(misc["Budget"],2))+  "</p>\n")
            except Exception as error:
                print(error)  
                f.close()
            finally:    
                f.close()
            return 1
    except Exception as error:
            print(error)
    finally:
        print("Loading...")

def endingReceipt(shopName:str)->None:
    """Prints at the End of the Receipt After the Transactions is Finished"""
    try:
        f = open('MiniProjects/PythonPOS/MultiPageVersion/receipt.html', 'a')
        f.write("<p>-------------------------------" + "<br>" + "\n" \
            + "Thank You <br> for Purchasing in <br>" + "\n"\
            + shopName + "!</p>" + "\n")
    except Exception as error:
        print(error)  
        f.close()    
    finally:
        f.close()

main()