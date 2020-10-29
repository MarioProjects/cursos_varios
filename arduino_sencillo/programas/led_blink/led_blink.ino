
// Creamos una variable que nos permitira saber en todo momento en que pin esta el LED
int LED = 7;

// la funcion setup corre una vez cuando enchufamos la placa o la reseteamos
void setup() {
  // Establecemos el Pin3 como salida.
  pinMode(LED , OUTPUT);
}
 
// la funcion loop corre una vez tras otra infinitamente
void loop() {
  digitalWrite(LED , HIGH);  // enchufamos el LED  estableciendo su voltaje a HIGH
  delay(500);                // esperamos 500ms 
  digitalWrite(LED , LOW);   // apagamos el LED  estableciendo su voltaje a LOW
  delay(1000);               // esperamos 1000ms (1s)
}
