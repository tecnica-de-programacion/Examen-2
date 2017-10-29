
int perillaX = A0;
int perillaY = A1;
int potval = 0;
int mapval = 0;

void setup(){
  Serial.begin(115200);
}

void loop(){
  int perilla_Val = analogRead(perillaX);
  sendData(perilla_Val);
}

void sendData(int value){
  mapval = map(value, 0, 1023, 0, 500);
  Serial.print(value);
  Serial.print(",");
  Serial.println(mapval);
  delay(100);
}


