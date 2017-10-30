int A_0 = 0; 
int A_1 = 1; 
int val_X = 0; 
int val_Y = 0; 

void loop(){
      val_X=analogRead(A_0);
      Serial.print(val_X);
      Serial.print(',');
      val_Y=analogRead(A_1);
      Serial.println(val_Y);
      delay(20);
}

void setup(){
      Serial.begin(115200);
}


