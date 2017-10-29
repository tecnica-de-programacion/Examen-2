
int sensorPin0 = A0;
int sensorPin1 = A1;
int potValue = 0;
int mapValue = 0;

void setup() {
   Serial.begin(115200);
}

void loop() {
  int sensorValueHorizontal = analogRead(sensorPin0);
  sendDataHorizontal(sensorValueHorizontal);
  int sensorValueVertical = analogRead(sensorPin1);
  sendDataVertical(sensorValueVertical);
}

void sendDataHorizontal(int value) {
  mapValue = map(value, 0, 1023, 0, 400);
  Serial.print("Horizontal");
  Serial.print(",");
  Serial.print(value);
  Serial.print(",");
  Serial.println(mapValue);
}

void sendDataVertical(int value) {
  mapValue = map(value, 0, 1023, 0, 400);
  Serial.print("Vertical");
  Serial.print(",");
  Serial.print(value);
  Serial.print(",");
  Serial.println(mapValue);
}
