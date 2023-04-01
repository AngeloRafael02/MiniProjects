
/*DEVNOTE:
BUGS Still to be fixed:
Decimals only work once, find a way to repeat it another time for the second number 
*/

#include <Keypad.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 2); // set the LCD address to 0x27 for a 16 chars and 2 line display

const byte ROWS = 4;
const byte COLS = 4;

char keys [ROWS] [COLS] = {
  {'1', '2', '3', '+'},
  {'4', '5', '6', '-'},
  {'7', '8', '9', '*'},
  {'.', '0', '=', '/'} 
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
float Answer;

void loop() {
  
  char key = myKeypad.getKey();
  if (key != NO_KEY){
     lcd.clear();
     lcd.setCursor(0,0);
     lcd.print(display += key);
     if (key == '='){ //main computing logic block
        String firstNumStr = display.substring(0, operationIndex(display)); //gets first number in string
        float firstNum = firstNumStr.toFloat();                             //parses it to float

        String secondNumStr = display.substring(operationIndex(display)+1); //gets second number in string
        float secondNum = secondNumStr.toFloat();                           //parses it to float
        
        lcd.setCursor(0,1);
        Answer = calculate(display,firstNum,secondNum);  //Calculates Input
        lcd.print(Answer);                 
        pinMode(2,HIGH);
     }
     if ((key == keys[0][3] || key == keys[1][3] || key == keys[2][3] || key == keys[3][3]) && Answer != NULL){
        lcd.clear();
        lcd.setCursor(0,0);
        display = Answer;  
        lcd.print(display + key);
        display += key;
        lcd.setCursor( display.length(),0);
     }
     switch(key){ ///This code somehow prevents repetition of operations, switching them instead, voltage is HIGH again after pressing
       case '+': disableRepeat(keys[0][3],display);
       case '-': disableRepeat(keys[1][3],display);
       case '*': disableRepeat(keys[2][3],display);
       case '/': disableRepeat(keys[3][3],display); pinMode(2,LOW); break;
       case '.': keys[3][0]=NULL; disableRepeat('.',display);
     }
   }
}
int operationIndex(String equation){
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
    result = equation.indexOf('/');
    return result;   
  }
  return result;
}

float calculate(String operation, float num1, float num2){
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
void disableRepeat(char input, String Sentence){ 
    if (Sentence.indexOf(input)!=Sentence.lastIndexOf(input)){
    display.remove(display.length()-1);
  }
}
