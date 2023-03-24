#include <Keypad.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 2); // set the LCD address to 0x27 for a 16 chars and 2 line display

const byte ROWS = 4;
const byte COLS = 4;

char keys [ROWS] [COLS] = {
  {'1', '2', '3', '+'},
  {'4', '5', '6', '-'},
  {'7', '8', '9', '*'},
  {'C', '0', '=', '/'} // C is to Cancel | "=" is to solve
};
byte rowPins[ROWS] = {9,8,7,6};
byte colPins[COLS] = {5,4,3,2};

Keypad myKeypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS ); 

void setup()
{
  lcd.init();                      
  lcd.backlight();
}

String display = "";

void loop() {
  
  char key = myKeypad.getKey();
  if (key != NO_KEY){
     lcd.clear();
     lcd.setCursor(0,0);
     lcd.print(display += key);
     if (key == '='){
        String firstNumStr = display.substring(0, operationIndex(display)); //gets first number in string
        float firstNum = firstNumStr.toFloat();                             //parses it to float

        String secondNumStr = display.substring(operationIndex(display)+1); //gets second number in string
        float secondNum = secondNumStr.toFloat();                           //parses it to float
        
        lcd.setCursor(0,1);
        lcd.print(calculate(display,firstNum,secondNum) );                  //Calculates Input
     }
     if (key == 'C'){     // C is CANCEL
       lcd.clear();       // clears lcd display 
       display = "";      // clears display variable 
       lcd.setCursor(0,0);// resets cursor
     }
   }
 
}

int operationIndex(String equation){ //finds an operator and returns its index from the string variable
  int result = -1;
  if (equation.indexOf('+') != -1){
    result = equation.indexOf('+'); 
    return  result;
  } else if (equation.indexOf('-') != -1){
    result = equation.indexOf('-');
    return result;    
  } else   if (equation.indexOf('*') != -1){
    result = equation.indexOf('*');
    return result;
  } else if (equation.indexOf('/') != -1){
    result = equation.indexOf('+');
    return result;   
  }
  return result; //cannot find any operator
}

float calculate(String operation, float num1, float num2){ //Calculates Input
  if (operation.indexOf('+') != -1){
    return  num1 + num2;
  } else if (operation.indexOf('-') != -1){
    return num1 - num2;    
  } else   if (operation.indexOf('*') != -1){
    return num1 * num2;
  } else if (operation.indexOf('/') != -1){
    return num1 / num2;   
  }
  return 0;
}

