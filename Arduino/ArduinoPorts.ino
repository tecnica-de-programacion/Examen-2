int sensorPin = A0;
int sensorPin2 = A1;
int potValue = 0;
int mapValue = 0;
int mapValue2 = 0;

void setup() {
  Serial.begin(115200);

}

void loop() {
  int sensorValue = analogRead(sensorPin);
  int sensorValue2 = analogRead(sensorPin2);
  sendData(sensorValue, sensorValue2);
  delay(50);

}

void sendData(int value, int value2){
  mapValue = map(value, 0, 1023, 3, 501);
  mapValue2 = map(value2, 0, 1023, 3, 601);
  Serial.print(value);
  Serial.print(",");
  Serial.print(mapValue);
  Serial.print(",");
  Serial.print(value2);
  Serial.print(",");
  Serial.println(mapValue2);
  
}

