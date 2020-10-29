int Digital_Pin = 3; 
  
void setup (){
  pinMode(Digital_Pin, INPUT);
  Serial.begin (9600); 
}
  
void loop (){  
  if(digitalRead(Digital_Pin) == HIGH)  {
      Serial.println("RUIDO!");
      delay(250);
  }
}
