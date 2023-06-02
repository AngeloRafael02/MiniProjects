//right
int Echo1 = A0;
int Trig1 = A1;
//left sensor
int Echo2 = A5;
int Trig2 = A4;
//middle sensor
int Echo3 = A3;
int Trig3 = A2;

const int LeftMotorForward = 7;
const int LeftMotorBackward = 6;
const int RightMotorForward = 4;
const int RightMotorBackward = 5;

const int ENA = 9;  // Adjust the pin number as per your setup
const int ENB = 10; // Adjust the pin number as per your setup

int ABS = 80;
int Left_Distance = 0, Right_Distance = 0, Middle_Distance = 0;

void moveForward() {
  digitalWrite(LeftMotorForward, HIGH);
  digitalWrite(RightMotorForward, HIGH);
  digitalWrite(LeftMotorBackward, LOW);
  digitalWrite(RightMotorBackward, LOW);
  analogWrite(ENA, ABS);
  analogWrite(ENB, ABS);
  Serial.print("ROBOT_MOVING_FORWARD");
}

void moveBackward() {
  digitalWrite(LeftMotorForward, LOW);
  digitalWrite(RightMotorForward, LOW);
  digitalWrite(LeftMotorBackward, HIGH);
  digitalWrite(RightMotorBackward, HIGH);
  analogWrite(ENA, ABS);
  analogWrite(ENB, ABS);
  Serial.print("ROBOT_MOVING_BACKWARD");
}

void moveLeft() {
  digitalWrite(LeftMotorForward, LOW);
  digitalWrite(RightMotorForward, HIGH);
  digitalWrite(LeftMotorBackward, LOW);
  digitalWrite(RightMotorBackward, LOW);
  analogWrite(ENA, ABS);
  analogWrite(ENB, ABS);
  Serial.print("ROBOT_MOVING_LEFT");
}

void moveRight() {
  digitalWrite(LeftMotorForward, HIGH);
  digitalWrite(RightMotorForward, LOW);
  digitalWrite(LeftMotorBackward, LOW);
  digitalWrite(RightMotorBackward, LOW);
  analogWrite(ENA, ABS);
  analogWrite(ENB, ABS);
  Serial.print("ROBOT_MOVING_RIGHT");
}

void moveStop() {
  digitalWrite(LeftMotorForward, LOW);
  digitalWrite(RightMotorForward, LOW);
  digitalWrite(LeftMotorBackward, LOW);
  digitalWrite(RightMotorBackward, LOW);
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
  Serial.print("ROBOT_STOP");
}

void moveCircleleft() {
  digitalWrite(LeftMotorForward, HIGH);
  digitalWrite(RightMotorForward, LOW);
  digitalWrite(LeftMotorBackward, LOW);
  digitalWrite(RightMotorBackward, HIGH);
  analogWrite(ENA, ABS);
  analogWrite(ENB, ABS);
  Serial.print("ROBOT_Circleleft");
}

void moveCircleright() {
  digitalWrite(LeftMotorForward, LOW);
  digitalWrite(RightMotorForward, HIGH);
  digitalWrite(LeftMotorBackward, HIGH);
  digitalWrite(RightMotorBackward, LOW);
  analogWrite(ENA, ABS);
  analogWrite(ENB, ABS);
  Serial.print("ROBOT_Circleleft");
}

//Ultrasonic distance measurement:
int Left_Distance_test() {
  digitalWrite(Trig2, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig2, HIGH);
  delayMicroseconds(25);
  digitalWrite(Trig2, LOW);
  float Fdistance = pulseIn(Echo2, HIGH);
  Fdistance = Fdistance / 29 / 2;
  return (int)Fdistance;
}

int Middle_Distance_test() {
  digitalWrite(Trig3, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig3, HIGH);
  delayMicroseconds(25);
  digitalWrite(Trig3, LOW);
  float Fdistance = pulseIn(Echo3, HIGH);
  Fdistance = Fdistance / 29 / 2;
  return (int)Fdistance;
}

int Right_Distance_test() {
  digitalWrite(Trig1, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig1, HIGH);
  delayMicroseconds(25);
  digitalWrite(Trig1, LOW);
  float Fdistance = pulseIn(Echo1, HIGH);
  Fdistance = Fdistance / 29 / 2;
  return (int)Fdistance;
}

void setup() {
  Serial.begin(9600);
  pinMode(Echo1, INPUT);
  pinMode(Trig1, OUTPUT);
  pinMode(Echo2, INPUT);
  pinMode(Trig2, OUTPUT);
  pinMode(Echo3, INPUT);
  pinMode(Trig3, OUTPUT);
  pinMode(RightMotorForward, OUTPUT);
  pinMode(LeftMotorForward, OUTPUT);
  pinMode(LeftMotorBackward, OUTPUT);
  pinMode(RightMotorBackward, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  moveStop();
}



void loop() {
  Left_Distance = Left_Distance_test();
  delay(10);
  Middle_Distance = Middle_Distance_test();
  delay(10);
  Right_Distance = Right_Distance_test();
  delay(10);

  if (Middle_Distance <= 20) {
    if (Right_Distance > Left_Distance) {
      if ((Right_Distance <= 20) && (Left_Distance <= 20)) {
        moveBackward();
        delay(200);
        moveCircleright();
        delay(150);
      } else {
        moveRight();
      }
    } else if (Right_Distance < Left_Distance) {
      if ((Right_Distance <= 20) && (Left_Distance <= 20)) {
        moveBackward();
        delay(200);
        moveCircleleft();
        delay(150);
      } else {
        moveLeft();
      }
    }
  }else if (Right_Distance <=15) {
    moveLeft();
  }else if (Left_Distance <= 15) {
    moveRight();
  }else {
    moveForward();
  }
}