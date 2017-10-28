int sensorPinVertical = A0;
int sensorPinHorizontal = A1;
int potValue = 0;
int mapValue = 0;

void setup(){
  Serial.begin(115200);
}

void loop(){
  int sensorValueVertical = analogRead(sensorPinVertical);
  int sensorValueHorizontal = analogRead(sensorPinHorizontal);
  sendData(sensorValueVertical);
  sendData(sensorValueHorizontal);
  delay(100);
}

void sendData(int value){
  mapValue = map(value, 0, 1023, 0, 400);
  Serial.print(value);
  Serial.print(",");
  Serial.println(mapValue);
}

