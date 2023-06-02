#include <NewPing.h>        //Ultrasonic sensor function library. You must install this library

//our L298N control pins
const int LeftMotorForward = 7;
const int LeftMotorBackward = 6;
const int RightMotorForward = 4;
const int RightMotorBackward = 5;

#define sensorNumber 3
#define maximum_distance 200
#define tooNear 20
#define GuideRangeLimit 150

boolean goesForward = false;
int CenterScan = 100;
int LeftScan = 100;
int RightScan = 100;

const int ENA = 9;  // Adjust the pin number as per your setup
const int ENB = 10; // Adjust the pin number as per your setup

int ABS = 80;

NewPing sonar[sensorNumber] = //Sensor object array. 
{   
  NewPing(A0, A1, maximum_distance), //Sensor sonar[0]Center     
  NewPing(A2, A3, maximum_distance), //Sensor sonar[1] Left
  NewPing(A4, A5, maximum_distance), //Sensor sonar[2] Right (PRIMARY)
};

void setup(){
    pinMode(RightMotorForward, OUTPUT);
    pinMode(LeftMotorForward, OUTPUT);
    pinMode(LeftMotorBackward, OUTPUT);
    pinMode(RightMotorBackward, OUTPUT);
    CenterScan = readPing(0);
}

void loop(){
    delay(50);
    CenterScan = readPing(0);
    LeftScan = readPing(1);
    RightScan = readPing(2);

    if (CenterScan <= tooNear || LeftScan <= tooNear){
        turnRight(700);
        moveStop();
    } else if (RightScan <= tooNear) {
    
        turnLeft(700);
        moveStop();
    } else {
        moveForward();
    }
}



int readPing(int sensorIndex){
    delay(70);
    int cm = sonar[sensorIndex].ping_cm();
    if (cm==0){
        cm=250;
    }
    return cm;
}

void moveStop(){
    digitalWrite(RightMotorForward, LOW);
    digitalWrite(LeftMotorForward, LOW);
    digitalWrite(RightMotorBackward, LOW);
    digitalWrite(LeftMotorBackward, LOW);
    analogWrite(ENA, ABS);
    analogWrite(ENB, ABS);
}

void moveForward(){
    if(!goesForward){
        goesForward=true;
        digitalWrite(LeftMotorForward, HIGH);
        digitalWrite(RightMotorForward, HIGH);
        digitalWrite(LeftMotorBackward, LOW);
        digitalWrite(RightMotorBackward, LOW);
    }
}

void moveBackward(int duration){
    goesForward=false;
    digitalWrite(LeftMotorBackward, HIGH);
    digitalWrite(RightMotorBackward, HIGH);
    digitalWrite(LeftMotorForward, LOW);
    digitalWrite(RightMotorForward, LOW);
    analogWrite(ENA, ABS);
    analogWrite(ENB, ABS);
    delay(duration);
}

void turnRight(int duration){
    digitalWrite(LeftMotorForward, HIGH);
    digitalWrite(RightMotorBackward, HIGH);
    digitalWrite(LeftMotorBackward, LOW);
    digitalWrite(RightMotorForward, LOW);
    analogWrite(ENA, ABS);
    analogWrite(ENB, ABS);
    delay(duration);
    digitalWrite(LeftMotorForward, HIGH);
    digitalWrite(RightMotorForward, HIGH);
    digitalWrite(LeftMotorBackward, LOW);
    digitalWrite(RightMotorBackward, LOW);
}

void turnLeft(int duration){
    digitalWrite(LeftMotorBackward, HIGH);
    digitalWrite(RightMotorForward, HIGH);
    digitalWrite(LeftMotorForward, LOW);
    digitalWrite(RightMotorBackward, LOW);
    analogWrite(ENA, ABS);
    analogWrite(ENB, ABS);
    delay(duration);
    digitalWrite(LeftMotorForward, HIGH);
    digitalWrite(RightMotorForward, HIGH);
    digitalWrite(LeftMotorBackward, LOW);
    digitalWrite(RightMotorBackward, LOW);
}