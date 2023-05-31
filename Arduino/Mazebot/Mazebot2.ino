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
  delay(100);
  CenterScan = readPing(0);
  delay(100);
  CenterScan = readPing(0);
  delay(100);
  CenterScan = readPing(0);
  delay(100);
}

void loop(){
  delay(50);

  if (LeftScan <= tooNear){ 
    turnRight(100);
  }
  if (RightScan <= tooNear){
    turnLeft(100);
  }
  if (CenterScan <= tooNear){
    moveStop();
    delay(300);
    moveBackward();
    delay(400);
    moveStop();
    delay(300);

    if (LeftScan >= RightScan){
      turnLeft(700);
      moveStop();
    }
    else{
      turnRight(700);
      moveStop();
    }
  }
  else{
    moveForward();
  }
    CenterScan = readPing(0);
    LeftScan = readPing(1);
    RightScan = readPing(2);
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

void moveBackward(){
  goesForward=false;
  digitalWrite(LeftMotorBackward, HIGH);
  digitalWrite(RightMotorBackward, HIGH);
  digitalWrite(LeftMotorForward, LOW);
  digitalWrite(RightMotorForward, LOW);
}

void turnRight(int duration){

  digitalWrite(LeftMotorForward, HIGH);
  digitalWrite(RightMotorBackward, HIGH);
  digitalWrite(LeftMotorBackward, LOW);
  digitalWrite(RightMotorForward, LOW);
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
  delay(duration);
  digitalWrite(LeftMotorForward, HIGH);
  digitalWrite(RightMotorForward, HIGH);
  digitalWrite(LeftMotorBackward, LOW);
  digitalWrite(RightMotorBackward, LOW);
}