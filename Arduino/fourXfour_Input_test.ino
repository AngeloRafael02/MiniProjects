#include <LiquidCrystal_I2C.h>

#include <Keypad.h>

const byte ROWS = 4;
const byte COLS = 4;
char keys [ROWS] [COLS] = {
  {'1', '2', '3', '+'},
  {'4', '5', '6', '-'},
  {'7', '8', '9', '*'},
  {'C', '0', '=', '/'}
};
byte rowPins[ROWS] = {10, 9, 7, 6};
byte colPins[COLS] = {5, 4, 3, 2};

LiquidCrystal_I2C lcd(0x27, 20, 2
); // set the LCD address to 0x27 for a 16 chars and 2 line display
Keypad myKeypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

boolean presentValue = false;
boolean final = false; // flag to indicate whether the final answer is displayed
String num1 = ""; // variable to store the first number
String num2 = ""; // variable to store the second number
int answer = 0; // variable to store the answer
char op = '+'; // variable to store the operator, default is addition

void setup()
{
  lcd.init();                      
  lcd.backlight();
  lcd.setCursor(3,0);
  lcd.print("GROUP-6");
  lcd.setCursor(3,1);
  lcd.print("Calculator");
  delay(3000);
  lcd.clear();
}
void loop() {
  char key = myKeypad.getKey();

  if (key != NO_KEY && (key == '1' || key == '2' || key == '3' || key == '4' || key == '5' || key == '6' || key == '7' || key == '8' || key == '9' || key == '0'))
  {
    if (final == true) // check if final answer is displayed
    {
      num1 = ""; // reset num1 to start new calculation
      num1 = num1 + key;
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("INSERT FIRST NUM:");
      lcd.setCursor(0, 1);
      lcd.print(num1);
      final = false; // reset final flag
    }
    else if (presentValue != true)
    {
      num1 = num1 + key;
      int numLength = num1.length();
      lcd.setCursor(0, 0);
      lcd.print("INSERT FIRST NUM:");
      lcd.setCursor(0, 1);
      lcd.print(num1);
    }
    else
    {
      num2 = num2 + key;
      int numLength = num2.length();
      lcd.setCursor(0, 0);
      lcd.print("INSERT 2ND NUM: ");
      lcd.setCursor(0, 1);
      lcd.print(num2);
    }
  }

 // If the key is an operator
else if (key != NO_KEY && (key == '+' || key == '-' || key == '*' || key == '/'))
{
if (num1 != "") // check if num1 is not empty
{
op = key;
presentValue = true; // set flag to indicate second number input
lcd.clear();
lcd.setCursor(0, 0);
lcd.print("INSERT 2ND NUM: ");
lcd.setCursor(0, 1);
lcd.print(num2);
}
}

// If the key is the equal sign
else if (key != NO_KEY && key == '=')
{
if (num1 != "" && num2 != "") // check if both num1 and num2 are not empty
{
int n1 = num1.toInt(); // convert num1 to integer
int n2 = num2.toInt(); // convert num2 to integer
 switch (op) // perform the calculation based on the operator
  {
    case '+':
      answer = n1 + n2;
      break;
    case '-':
      answer = n1 - n2;
      break;
    case '*':
      answer = n1 * n2;
      break;
    case '/':
      answer = n1 / n2;
      break;
  }

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("ANSWER:");
  lcd.setCursor(0, 1);
  lcd.print(answer);
  final = true; // set flag to indicate final answer is displayed
  presentValue = false; // reset flag for second number input
  num1 = ""; // reset num1
  num2 = ""; // reset num2
}
// If the key is an operator
else if (key != NO_KEY && (key == '+' || key == '-' || key == '*' || key == '/'))
{
if (num1 != "") // check if num1 is not empty
{
op = key;
presentValue = true; // set flag to indicate second number input
lcd.clear();
lcd.setCursor(0, 0);
lcd.print("INSERT 2ND NUM: ");
lcd.setCursor(0, 1);
lcd.print(num2);
}
}

// If the key is the equal sign
else if (key != NO_KEY && key == '=')
{
if (num1 != "" && num2 != "") // check if both num1 and num2 are not empty
{
int n1 = num1.toInt(); // convert num1 to integer
int n2 = num2.toInt(); // convert num2 to integer
  switch (op) // perform the calculation based on the operator
  {
    case '+':
      answer = n1 + n2;
      break;
    case '-':
      answer = n1 - n2;
      break;
    case '*':
      answer = n1 * n2;
      break;
    case '/':
      answer = n1 / n2;
      break;
  }

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("ANSWER:");
  lcd.setCursor(0, 1);
  lcd.print(answer);
  final = true; // set flag to indicate final answer is displayed
  presentValue = false; // reset flag for second number input
  num1 = ""; // reset num1
  num2 = ""; // reset num2
}
}

// If the key is the clear button
else if (key != NO_KEY && key == 'C')
{
lcd.clear();
lcd.setCursor(3,0);
lcd.print("Maker UNO");
lcd.setCursor(3,1);
lcd.print("Calculator");
delay(3000);
lcd.clear();
num1 = ""; // reset num1
num2 = ""; // reset num2
answer = 0; // reset answer
op = '+'; // reset operator to addition
presentValue = false; // reset flag for second number input
final = false; // reset final flag
}
}
}