int draw_vertical = A1;
int draw_horizontal = A2;
int mapValue = 0;
int mapValue2 = 0;

void setup() {
   Serial.begin(115200);
}

void loop() {
  int sensorValue = analogRead(draw_vertical); 
  int sensorValue2 = analogRead(draw_horizontal);
  sendData(sensorValue, sensorValue2);
}

void sendData(int value, int value2) {
  mapValue = map(value, 0, 1023, 0, 600);
  mapValue2 = map(value2, 0, 1023, 0, 600);
  Serial.print(mapValue);
  Serial.print(",");
  Serial.println(mapValue2);
  delay(100);
}

