
const int ledPin = 13;//the led attach to

void setup()
{
  pinMode(ledPin,OUTPUT);//initialize the ledPin as an output
  pinMode(2,INPUT);
  digitalWrite(2, HIGH);
  Serial.begin(9600);
}
/******************************************/
void loop()
{
  int digitalVal = digitalRead(2);
  if(HIGH == digitalVal)
  {
    digitalWrite(ledPin,LOW);//turn the led off
    Serial.println("El sensor está en horizontal");
  }
  else
  {
    digitalWrite(ledPin,HIGH);//turn the led on
    Serial.println("El sensor está en vertical");
  }
}
