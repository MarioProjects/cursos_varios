
//Constantes:
const int ledPin = 9;  // Pin pin 9 tiene PWM para asignar valores al LED
const int potPin = A0; // Pin A0 para leer valores analogicos

//Variables:
int value; // Para guardar el valor del potenciometro


void setup(){
  Serial.begin(9600); //Iniciamos La comunicacion serial
  pinMode(ledPin, OUTPUT); 
  pinMode(potPin, INPUT); //Optional 
}

void loop(){  
  value = analogRead(potPin);          // Leemos y almacenamos el valor del potenciometro
  Serial.println(value);               // Lo imprimimos en la pantalla serial
  value = map(value, 0, 1023, 0, 255); // Mapeamos el valor de 0-1023 a 0-255 (PWM)
  analogWrite(ledPin, value);          // Mandamos el valor al led
  delay(10);                          // Ponemos un poco de espera para apreciar los cambios
}
