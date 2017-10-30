int sensorPin0 = A0;
int sensorPin1 = A1;
int mapValueHorizontal = 0;
int mapValueVertical = 0;

void setup() {
   Serial.begin(115200);
}

void loop() {
  int sensorValueHorizontal = analogRead(sensorPin0);
  int sensorValueVertical = analogRead(sensorPin1);
  sendData(sensorValueHorizontal, sensorValueVertical);
  delay(100);
}

void sendData(int valueHorizontal, int valueVertical) {
  mapValueHorizontal = map(valueHorizontal, 0, 1023, 0, 600);
  mapValueVertical = map(valueVertical, 0, 1023, 0, 500);
  Serial.print("Horizontal");
  Serial.print(",");
  Serial.print(mapValueHorizontal);
  Serial.print(",");
  Serial.print("Vertical");
  Serial.print(",");
  Serial.println(mapValueVertical);
}

