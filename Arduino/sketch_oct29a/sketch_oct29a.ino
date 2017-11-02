int leftsensor =  A0;
int rightsensor = A1;
int leftpotValue =  0;
int rightpotValue = 0;
int mapValue = 0;

void setup() {
   Serial.begin(115200);
}

void loop() {
  int rightpotsenValue = analogRead(rightsensor);
  int leftpotsenValue =  analogRead(leftsensor);
  sendData(leftpotsenValue, true);
  sendData(rightpotsenValue, false);
  delay(100);
}

void sendData(int value) {
  mapValue = map(value, 0, 1023, 0, 400);
  Serial.print(value);
  Serial.print(",");
  Serial.println(mapValue);
}
