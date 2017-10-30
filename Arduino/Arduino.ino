int sensorPot1 = A1;
int sensorPot2 = A2;
int potValue1 = 0;
int potValue2 = 0;
int mapValueVertical = 0;
int mapValueHorizontal = 0;

void setup(){
  Serial.begin(115200);
}

void loop(){
  delay(70);
  int sensorValue1 = analogRead(sensorPot1);
  int sensorValue2 = analogRead(sensorPot2);
  sendData(sensorValue1,sensorValue2);

}

void sendData(int vertical, int horizontal){
  mapValueVertical = map(vertical, 0, 1023, 0, 500);
  mapValueHorizontal = map(horizontal, 0, 1023, 0, 600);
  String str_ver = String(mapValueVertical);
  String str_hor = String(mapValueHorizontal);
  if (str_ver.length()<2){
    str_ver = "0" + String(mapValueVertical);
  }
  if (str_hor.length()<2){
    str_hor = "0" + String(mapValueHorizontal);
  }
  Serial.print(str_ver);
  Serial.print(",");
  Serial.println(str_hor);
}

