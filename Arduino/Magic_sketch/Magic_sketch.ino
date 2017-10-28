int sensorPinVertical = A0;
int sensorPinHorizontal = A1;
int mapValueVertical = 0;
int mapValueHorizontal = 0;
int height = 500;
int width = 600;

void setup(){
  Serial.begin(115200);
}

void loop(){
  int sensorValueVertical = analogRead(sensorPinVertical);
  int sensorValueHorizontal = analogRead(sensorPinHorizontal);
  sendData(sensorValueVertical, sensorValueHorizontal);
  delay(100);
}

void sendData(int valueVertical, int valueHorizontal){
  mapValueVertical = map(valueVertical, 0, 1023, 0, height);
  mapValueHorizontal = map(valueHorizontal, 0, 1023, 0, width);
  Serial.print(valueVertical);
  Serial.print(",");
  Serial.print(valueHorizontal);
  Serial.print(",");
  Serial.print(mapValueVertical);
  Serial.print(",");
  Serial.println(mapValueHorizontal);
}

