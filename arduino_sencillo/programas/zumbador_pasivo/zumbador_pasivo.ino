const int buzzer = 9; // zumbador en el pin 9

void setup(){
  pinMode(buzzer, OUTPUT); // Definimos el pin 9 del zumbador como salida
}

void loop(){
  tone(buzzer, 1000); // Mnadamos una señal de sonido de 1KHz...
  delay(1000);        // esperamos 1 segundo
  noTone(buzzer);     // Paramos el sonido...
  delay(1000);        // esperamos 1 segundo
}
