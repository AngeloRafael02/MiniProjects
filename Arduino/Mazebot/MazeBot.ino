#include <NewPing.h>        //Ultrasonic sensor function library. You must install this library

//our L298N control pins
const int LeftMotorForward = 7;
const int LeftMotorBackward = 6;
const int RightMotorForward = 4;
const int RightMotorBackward = 5;

#define sensorNumber 3
#define maximum_distance 200
#define tooNear 20

boolean goesForward = false;
int CenterScan = 100;
int LeftScan = 100;
int RightScan = 100;

NewPing sonar[sensorNumber] = //Sensor object array. 
{   
  NewPing(A0, A1, maximum_distance), //Sensor sonar[0]Center     
  NewPing(A2, A3, maximum_distance), //Sensor sonar[1] Left
  NewPing(A4, A5, maximum_distance), //Sensor sonar[2] Right
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

// MAIN LOGIC: Which ever side sensor detects more space/distance is followed
void loop(){
  CenterScan = readPing(0);
  LeftScan = readPing(1);
  RightScan = readPing(2);
  delay(50);

  //Adjusts Sides to prevent side collisions
  if (LeftScan <= tooNear){ 
    turnRight(100);
  }
  if (RightScan <= tooNear){
    turnLeft(100);
  }

  if (CenterScan <= tooNear){ //Procs when CenterSensors is near an object
    moveStop();
    delay(300);
    moveBackward();
    delay(400);
    moveStop();
    delay(300);

    if (LeftScan >= RightScan){ // Compares value of Left Sensor and Right Sensor to determine which way to go
      turnLeft(700);
      moveStop();
    }
    else{
      turnRight(700);
      moveStop();
    }

    if (LeftScan <= tooNear && RightScan <= tooNear){ //Procs when all sides are in near an object
      turnLeft(1500); //Hypothetically a near 180 degree turn 
    }
  }
  else{
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
   // "duration" parameter determines how much time does the motor turn (more time = more turns)
  digitalWrite(LeftMotorForward, HIGH);
  digitalWrite(RightMotorBackward, HIGH);
  digitalWrite(LeftMotorBackward, LOW);
  digitalWrite(RightMotorForward, LOW);
  delay(duration);
  //goes back to MoveForward Configuration
  digitalWrite(LeftMotorForward, HIGH);
  digitalWrite(RightMotorForward, HIGH);
  digitalWrite(LeftMotorBackward, LOW);
  digitalWrite(RightMotorBackward, LOW);
}


void turnLeft(int duration){
  // "duration" parameter determines how much time does the motor turn (more time = more turns)
  digitalWrite(LeftMotorBackward, HIGH);
  digitalWrite(RightMotorForward, HIGH);
  digitalWrite(LeftMotorForward, LOW);
  digitalWrite(RightMotorBackward, LOW);
  delay(duration);
  //goes back to MoveForward Configuration
  digitalWrite(LeftMotorForward, HIGH);
  digitalWrite(RightMotorForward, HIGH);
  digitalWrite(LeftMotorBackward, LOW);
  digitalWrite(RightMotorBackward, LOW);

}