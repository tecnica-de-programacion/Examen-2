int sensor_pin_Vertical = A0; 
int sensor_pin_Horizontal = A1;
int potVertical = 0;
int potHorzizontal = 0;
int mapVertical= 0;
int mapHorizontal = 0;

void setup() {
   Serial.begin(115200);
}

void loop() {
  delay(80);
  int sensor_value_Vertical = analogRead(sensor_pin_Vertical);
  int sensor_value_Horizontal = analogRead(sensor_pin_Horizontal); 
  sendData(sensor_value_Vertical,sensor_value_Horizontal);
  
}

void sendData(int valueV, int valueH) {
  mapVertical = map(valueV, 0, 1023, 0, 500);
  mapHorizontal = map(valueH, 0, 1023, 0, 600);
  String mapver_string = String(mapVertical);
  if (mapver_string.length() < 2) {
     mapver_string =  "0" + String(mapVertical);
     
  }
  Serial.print(mapver_string);
  Serial.print(" ");
  Serial.println(mapHorizontal);
}
