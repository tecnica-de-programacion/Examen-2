int Pot_horizontal = A1;
int Pot_vertical = A2;
int potValue = 0;
int mapValue_horizontal = 0;
int mapValue_vertical = 0;

void setup() {
   Serial.begin(115200);
}

void loop() {
  int Pot_horizontal_Value = analogRead(Pot_horizontal); 
  int Pot_vertical_Value = analogRead(Pot_vertical);
  sendData(Pot_horizontal_Value, Pot_vertical_Value);
}

void sendData(int horizontal, int vertical) {
  mapValue_horizontal = map(horizontal, 0, 1023, 0, 600);
  mapValue_vertical = map(vertical, 0, 1023, 0, 500);
  Serial.print( mapValue_horizontal);
  Serial.print(",");
  Serial.print(mapValue_vertical);
  Serial.println("");
  delay(100);
}
