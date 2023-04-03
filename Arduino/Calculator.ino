/*DEV-NOTE:
FIXED: Decimals only work once, find a way to repeat it another time for the second number 
FIXED*:pressing '=' after input one number (no operation chose yet) does bugs
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
  {'.', '0', NULL, '/'} };
byte rowPins[ROWS] = {9,8,7,6};
byte colPins[COLS] = {5,4,3,2};

Keypad myKeypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS ); 

String display = "";
float Answer;

void setup(){
  lcd.init();                      
  lcd.backlight();
}
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
      Answer = calculate(display,firstNum,secondNum); //Calculates Input
      lcd.print(Answer);


      //resets operator keys default value      
      keys[0][3]='+';
      keys[1][3]='-';
      keys[2][3]='*';
      keys[3][3]='/'; 
      //disables numbers temporarily until operator is picked
      for ( int row0 = 0; row0 < 4; ++row0 ){
        keys[ row0 ][ 0 ] = NULL;
        keys[ row0 ][ 1 ] = NULL;
        keys[ row0 ][ 2 ] = NULL;
      }
    }
    if (key == keys[0][3] || key == keys[1][3] || key == keys[2][3] || key == keys[3][3]){
      ///This code somehow prevents repetition of operations, state is normal again after pressing '='
      keys[0][3]=NULL;
      keys[1][3]=NULL;
      keys[2][3]=NULL;
      keys[3][3]=NULL; 
      keys[3][0]='.';
      keys[3][2]='=';
      if (Answer != NULL){
        KeypadStateNormal();
        lcd.clear();
        lcd.setCursor(0,0);
        display = Answer;  
        lcd.print(display + key);
        display += key;
        lcd.setCursor( display.length(),0);         
      }
    }
    if(key =='.'){
      //this block code prevents repitition of decimal point
     keys[3][0]=NULL;
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

void KeypadStateNormal(){
  keys[0][0]='1'; keys[0][1]='2'; keys[0][2]='3'; 
  keys[1][0]='4'; keys[1][1]='5'; keys[1][2]='6'; 
  keys[2][0]='7'; keys[2][1]='8'; keys[2][2]='9'; 
  keys[3][0]='.'
}