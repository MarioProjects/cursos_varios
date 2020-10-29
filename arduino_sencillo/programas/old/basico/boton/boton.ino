// Las 'constants' no cambian
const int buttonPin = 2;     // El pin donde conectamos el boton

// Las variables que pueden cambiar 
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  Serial.begin(9600);  // Nos comunicaremos con el ordenador para mostrar el estado del boton
  pinMode(buttonPin, INPUT); // Definimos el pin donde esta el boton como una entrada
}

void loop() {
  // Leemos el estado del boton y lo guardamos en una variable
  buttonState = digitalRead(buttonPin);
 
  // Comprobamos si el boton esta presionado
  // Si esta presionado su estado es HIGH:
  if (buttonState == HIGH) {
    // El boton esta siendo presionado
    Serial.println(buttonState);
  } else {
    // El boton NO esta siendo presionado
    Serial.println(buttonState);
  }

  // Añadimos una pausa para poder ver fácilmente el estado del boton
  delay(100);

}
