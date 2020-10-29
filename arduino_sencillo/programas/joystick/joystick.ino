int ladoy = A0; // Entrada de referencia para el eje de las Y's.
int ladox = A1; // Entrada de referencia para el eje de las X's.
int valor, valor2;

void setup() {
  Serial.begin(9600);
}
 
void loop() {

  // El valor central para el eje x es de 500 y su minimo 0 y maximo 1023
  valor = analogRead(ladox); // Durante todo el proceso interrogaremos
  
  if (valor > 775){ // el valor en el que se encuentra posicionado
    // así asignaremos una acción para una posicion deseada.
    Serial.println("Derecha");
  } else if (valor < 240){
    Serial.println("Izquierda");
  } else{
    Serial.println("Centro");
  }

  // El valor central para el eje y es de 500 y su minimo 0 y maximo 1023
  valor2 = analogRead(ladoy);
  
  if (valor2 > 775){ // el valor en el que se encuentra posicionado
    // así asignaremos una acción para una posicion deseada.
    Serial.println("Arriba");
  } else if (valor2 < 240){
    Serial.println("Abajo");
  } else{
    Serial.println("Centro");
  }
  
}
