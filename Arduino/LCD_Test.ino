#include <Wire.h>
#include<LiquidCrystal.h>

int buttonPin = 9;
int passFlag = 0;
const unsigned long eventInterval = 300;
unsigned long previousTime = 0;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int initial = 0;
int oldState = 0;
int buttonState = 0;

void setup(){
 lcd.begin(16, 2); 
  pinMode(buttonPin, INPUT);
}

void loop(){
    unsigned long currentTime = millis();
    buttonState = digitalRead(buttonPin);
    if (buttonState == HIGH) {
        delay(50);
        buttonState = digitalRead(buttonPin);
        if (buttonState == LOW) {
            initial = oldState + 1;
            passFlag = 0;
        }
    } else {
        delay(100);
    }

    switch (initial) {
        case 1:
            if (passFlag == 0) {
                hello();
                passFlag++;                     // Increment passFlag
            }
            oldState = initial;
            break;
        case 2:
            if (passFlag == 0) {
                hi();
                passFlag++;                     // Increment passFlag
            }
            oldState = initial;
            break;
        case 3:
            if (passFlag == 0) {
                hola();
                passFlag++;                     // Increment passFlag
            }
            while(digitalRead(buttonPin) != HIGH){
                currentTime = millis();
                if (currentTime - previousTime >= eventInterval){
                lcd.scrollDisplayLeft();
                previousTime = currentTime;
                }
            }
            oldState = initial;
            break;
        default:
            lcd.clear();
            oldState = 0;
            break;
    }
}

void hello() {
  lcd.clear();
  lcd.print(" HELLO, WORLD!");
  lcd.setCursor(0, 1);
  lcd.print("    ARDUINO");
  lcd.setCursor(17, 1);
}

void hi() {
  lcd.clear();
  lcd.print("KYLA T. LLANES");
  lcd.setCursor(0, 1);
  lcd.print("     CPE3-A");
  lcd.setCursor(17, 1);
}

void hola() {
  lcd.clear();
  lcd.print("  MIDORI :(");   
  }