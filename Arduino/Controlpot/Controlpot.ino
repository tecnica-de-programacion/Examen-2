int potenciometroX_pin=A0; 
int potenciometroY_pin=A1; 
int mapValueX=0;
int mapValueY=0;

void setup(){
  Serial.begin(115200);
}

void loop(){
  int sensorValueX=analogRead(potenciometroX_pin);
  sendDataX(sensorValueX);
  
  int sensorValueY=analogRead(potenciometroY_pin);
  sendDataY(sensorValueY);

  delay(100);
}
void sendDataX( int Xvalue) {
  mapValueX = map(Xvalue,0,1023,0,600);
  Serial.print(Xvalue);
  Serial.print(',');
  Serial.print(mapValueX);
  Serial.print(',');
  }
void sendDataY(int Yvalue) {
  mapValueY = map(Yvalue,0,1023,0,500);
  Serial.print(Yvalue);
  Serial.print(',');
  Serial.println(mapValueY);
  
}

