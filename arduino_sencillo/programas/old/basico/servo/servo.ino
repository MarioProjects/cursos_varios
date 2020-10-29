
#include <Servo.h>

Servo myservo;  // create servo object to control a servo

int val;    // variable to read the value from the analog pin
int dir = 0;
int pos;
void setup() {
  Serial.begin(9600);
  myservo.attach(A0);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  //varia la posicion de 0 a 120, con esperas de 15ms
   for (pos = 0; pos <= 120; pos += 1) 
   {
      myservo.write(pos);              
      delay(15);                       
   }
 
   //varia la posicion de 0 a 120, con esperas de 15ms
   for (pos = 120; pos >= 0; pos -= 1) 
   {
      myservo.write(pos);              
      delay(15);                       
   }
}
