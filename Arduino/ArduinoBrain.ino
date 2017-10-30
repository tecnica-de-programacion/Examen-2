int leftPotentiometer =  A4;
int rightPotentiometer = A5;
int potLeftValue =  0;
int potRightValue = 0;
int mapValue =  0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int sensorLeftValue =  analogRead(leftPotentiometer);
  int sensorRightValue = analogRead(rightPotentiometer);
  sendData(sensorLeftValue, true);
  sendData(sensorRightValue, false);
  delay(100); // Mala Practica Utilizar Delay
}

void sendData(int value, bool isLeft) {
  bool isComplete = !isLeft;
  int windowLength = isLeft ? 500 : 600;
  mapValue = map(value, 0, 1023, 0, windowLength);
  Serial.print(mapValue);
  if(isComplete) {
    Serial.print("\n");
  }
  else {
    Serial.print(", ");
  }
}
