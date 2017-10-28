int sensorPin0 = A0;
int sensorPin1 = A1;
int potValue = 0;
int mapValue0 = 0;
int mapValue1 = 0;

void setup() {
   Serial.begin(115200);
}

void loop() {
  int sensorValue0 = analogRead(sensorPin0);
  int sensorValue1 = analogRead(sensorPin1); 
  sendData(sensorValue0, sensorValue1);
} 

void sendData(int value0, int value1) {
  mapValue0 = map(value0, 0, 1023, 0, 400);
  mapValue1 = map(value1, 0, 1023, 0, 400);
  Serial.print(mapValue0);
  Serial.print(",");
  Serial.println(mapValue1);
}
