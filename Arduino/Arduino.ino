int sensorPin1 = A0;
int sensorPin2 = A1;
int mapValue1 = 0;
int mapValue2 = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int sensorValue1 = analogRead(sensorPin1);
  int sensorValue2 = analogRead(sensorPin2);
  sendData(sensorValue1, sensorValue2);
  delay(100);
}

void sendData(int value1, int value2){
  mapValue1 = map(value1, 0, 1023, 0, 500);
  mapValue2 = map(value2, 0, 1023, 0, 600);
  Serial.print(value1);
  Serial.print(",");
  Serial.print(mapValue1);
  Serial.print(",");
  Serial.print(value2);
  Serial.print(",");
  Serial.println(mapValue2);    
}
