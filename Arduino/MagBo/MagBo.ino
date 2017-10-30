
int sensorPinX = A0;
int sensorPinY = A1;

void setup() {
   Serial.begin(115200);
}

void loop() {
  int sensorValueX = analogRead(sensorPinX);
  int sensorValueY =  analogRead(sensorPinY);
  delay(20);
  Serial.print(sensorValueX);
  Serial.print(",");
  Serial.println(sensorValueY);
}

