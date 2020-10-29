// las constantes no cambian, se utilizan para establecer numeros de pines utilizados:
const int buttonPin = 2;     // el numero del pin del boton

void setup() {
  Serial.begin(9600);
  // inicializamos el pin del boton como una entrada:
  pinMode(buttonPin, INPUT_PULLUP);
}
void loop() {
  // comrpobamos si el boton esta siendo presionado, cuando pasa esto su estado es HIGH
  if (digitalRead(buttonPin) == HIGH) {
    Serial.println("Presionado");
  }

  // Añadimos cierta estpera para poder ver la salida del boton de forma clara
  delay(100);
}
