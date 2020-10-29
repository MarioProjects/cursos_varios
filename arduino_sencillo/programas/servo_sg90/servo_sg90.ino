#include <Servo.h>

Servo servo;
int angle = 10;

void setup() {
  servo.attach(8);  // Indicamos que el servo esta conectado en el pin 8
  servo.write(angle);
}

void loop(){ 
  
  // Movemos desde 0 a 180 grado
  for(angle = 1; angle < 180; angle++){                                  
    servo.write(angle);               
    delay(5);                   
  } 
  
  // Movemos desde 180 a 0 grados
  for(angle = 180; angle > 10; angle--){                                
    servo.write(angle);           
    delay(20);       
  } 
  
}
