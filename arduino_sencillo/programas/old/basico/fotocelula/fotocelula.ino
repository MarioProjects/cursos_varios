const int sensorPin = A0; // Conectamos nuestra fotocelula al pin análogico A0
int lightVal;

void setup() {
  Serial.begin(9600);  // Nos comunicaremos con el ordenador para mostrar el estado de la fotoceula
}

void loop() {
  lightVal = analogRead(sensorPin); // Leemos el sensor de la fotocelula
  Serial.println(lightVal); // Imprimimos el valor de la fotocelula
  delay(500); // Esperamos medio segundo para que podamos leer correctamente el valor en el monitor
}
