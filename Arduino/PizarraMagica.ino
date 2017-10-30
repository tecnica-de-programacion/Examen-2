int sensorPinX = A0;
int potValue = 0;
int sensorPinY = A1;
int mapValueX = 0;
int mapValueY = 0;

void setup() {
   Serial.begin(9600);
}

void loop() {
  int sensorValueX = analogRead(sensorPinX); 
  int sensorValueY = analogRead(sensorPinY); 
  sendData(sensorValueX,sensorValueY);
}

void sendData(int valuex,int valuey) {
  mapValueX = map(valuex, 0, 1023, 0, 600);
  mapValueY = map(valuey, 0, 1023, 0, 500);
  Serial.print(mapValueX);
  Serial.print(",");
  Serial.print(mapValueY);
  Serial.println("");
}
