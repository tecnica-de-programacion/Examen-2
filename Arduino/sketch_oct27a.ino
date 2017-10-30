int leftPotenciometer = A0;
int rightPotenciometer = A1;
int portValue = 0;
int left_mapValue = 0;
int right_mapValue = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int left_value = analogRead(leftPotenciometer);
  int right_value = analogRead(rightPotenciometer);
  
  sendData(left_value, right_value);
  delay(100);

}

void sendData(int left_value, int right_value){
  left_mapValue = map(left_value, 1023, 0, 500, 0);
  right_mapValue = map(right_value, 1023, 0, 600, 0);
  Serial.print(left_mapValue);
  Serial.print(",");
  Serial.println(right_mapValue);
}

