int sensorPin = A0;
int secondsendorPin = A1;
int potValue = 0;
int mapValue = 0;
int secondmapvalue = 0;

void setup() {
   Serial.begin(115200);
}

void loop() {
  int sensorValue = analogRead(sensorPin); 
  int secondsendorValue= analogRead(secondsendorPin);
  sendData(sensorValue,secondsendorValue);
}

void sendData(int value, int othervalue) {
  mapValue = map(value, 0, 1023, 0, 1000);
  secondmapvalue= map(othervalue,0,1023,0,1000);
  
  Serial.print(mapValue);
  Serial.print(",");
  Serial.println(secondmapvalue);
}

