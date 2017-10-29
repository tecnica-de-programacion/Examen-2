int leftsensorPin =  A0;
int rightsensorPin = A1;
int leftpotValue =  0;
int rightpotValue = 0;
int mapValue =  0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int leftsensorValue =  analogRead(leftsensorPin);
  int rightsensorValue = analogRead(rightsensorPin);
  sendData(leftsensorValue, true);
  sendData(rightsensorValue, false);
  delay(100);
}

void sendData(int value, bool isLeft) {
  bool isComplete = !isLeft;
  int windowLength = isLeft ? 496 : 601;
  mapValue = map(value, 0, 1023, 3, windowLength);
  Serial.print(mapValue);
  if(isComplete) {
    Serial.print("\n");
  }
  else {
    Serial.print(",");
  }
}
