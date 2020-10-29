/**
 * Led RGB (ánodo común)
 */

// Creamos una variable que nos permitira saber en todo momento en que pines esta el LED
int pinRojo = 9;
int pinVerde = 6;
int pinAzul = 7;

void setup() {
  // Establecemos los pines como salida.
  pinMode(pinRojo, OUTPUT);
  pinMode(pinVerde, OUTPUT);
  pinMode(pinAzul, OUTPUT);
}

void loop() {
  setColor(255,0,0);
  delay(1000);
  setColor(0,255,0);
  delay(1000);
  setColor(155,150,110);
  delay(1000);
}

void setColor(int rojo, int verde, int azul){
  analogWrite(pinRojo, rojo);
  analogWrite(pinVerde, verde);
  analogWrite(pinAzul, azul);
}
