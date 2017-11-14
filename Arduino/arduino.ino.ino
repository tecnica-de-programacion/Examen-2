
int perillaX = A0;
int perillaY = A1;
int mapvalH = 0;
int mapvalY = 0;
int pot_val = 0;

void setup(){
  Serial.begin(115200);
}

void loop(){
  int perilla_x_Val = analogRead(perillaX);
  int perilla_y_Val = analogRead(perillaY);
  sendData(perilla_x_Val, perilla_y_Val);
  
}

void sendData(int value_X, int value_Y){
  mapvalH = map(value_X,0, 1023, 0, 600);
  mapvalY = map(value_Y,0, 1023, 0, 500);
  Serial.print(mapvalH);
  Serial.print(",");
  Serial.print(mapvalY);
  Serial.println("");
  delay(100);

}


