# RECIO, Angelo Rafael
# 11/02/2022
# 3:30 PM

try:
    def repeat():
        again = str(input("Do you want to repeat the program? y/n "))
        if again == "y" or again  == "Y":
            Calculator()
        elif again == "n" or again == "N":
            print("Thank you for using the program!")

    def Calculator(num1, num2, ope):
        """
                            ***BASIC ARITHMETIC CAlCULATOR***
        This is a code that can do basic addition, suntraction, multiplication, division.
        Operator Inputs: 
        Addition: +     Subtraction: -       Multiplication: *      Division : /
        """
        if (ope == "+"):
            num3 = num1 + num2
            result1 = f"{num1} + {num2} = {num3}"
            print(result1)
            repeat()
        elif (ope == "-"):
            num3 = num1 - num2
            result1 = f"{num1} - {num2} = {num3}"
            print(result1)
            repeat()
        elif (ope == "*"):
            num3 = num1 * num2
            result1 = f"{num1} * {num2} = {num3}"
            print(result1)
            repeat()
        elif (ope == "/"):
            num3 = num1 // num2
            result1 = f"{num1} / {num2} = {num3}"
            print(result1)
            repeat()
        else:
            return "Error: please enter your operation according to the instructions."

    print(Calculator.__doc__)
    print(Calculator(num1 = float(input("Enter First Number: ")),\
                    num2 = float(input("Enter Second Number: ")),\
                    ope = str(input("Choose Operation: "))))

except ValueError:
    print("Error: Please enter the correct data.")
except ZeroDivisionError:
    print("Error: Program cannot divide by zero.")
except Exception as error: 
    print(error)
finally:
    print('Program Finished! Thank you for using the program.')