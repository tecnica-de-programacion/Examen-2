int sensorPin_x = A0; 
int sensorPin_y = A1; 
int line_x = 0; 
int line_y = 0; 

void setup(){
   Serial.begin(115200);
}

void loop() {
  int sensorValue_x = analogRead(sensorPin_x); 
  sendData_x(sensorValue_x);
  int sensorValue_y = analogRead(sensorPin_y); 
  sendData_y(sensorValue_y);
}

void sendData_x(int value){
      line_x = map(value, 0, 1023, 0, 600);
      Serial.print(value);
      Serial.print(",");
      Serial.print(line_x);
      Serial.print(",");
      delay (30);
}

void sendData_y(int value){
      line_y = map(value, 0, 1023, 0, 500);
      Serial.print(value);
      Serial.print(",");
      Serial.println(line_y);
      delay (30);
}
 
