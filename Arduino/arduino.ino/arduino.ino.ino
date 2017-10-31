
int perillaX = A0;
int perillaY = A1;
int mapvalH = 0;
int mapvalY = 0;

void setup(){
  Serial.begin(115200);
}

void loop(){
  int perilla_x_Val = analogRead(perillaX);
  int perilla_y_Val = analogRead(perillaY);
  sendData(perilla_x_Val, perilla_y_Val);
  delay(100);
}

void sendData(int value_X, int value_Y){
  mapvalH = map(value_X,1023, 0, 600, 0);
  mapvalY = map(value_Y,1023, 0, 500, 0);
  Serial.print(value_X);
  Serial.print(",");
  Serial.print(value_Y);

}


