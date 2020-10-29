const int buzzer = 9; //Ponemos el zumbador en el pin 9
const int buttonPin = 2;     // El pin donde conectamos el boton

int buttonState = 0;         // variable for reading the pushbutton status

void setup(){
 
  pinMode(buzzer, OUTPUT); // Indicamos que el pin del zumbador debe ser tratado como una salida
  pinMode(buttonPin, INPUT); // Definimos el pin donde esta el boton como una entrada
}

void loop(){
 
 // Leemos el estado del boton y lo guardamos en una variable
  buttonState = digitalRead(buttonPin);
 
  // Comprobamos si el boton esta presionado
  // Si esta presionado su estado es HIGH:
  if (buttonState == HIGH) {
    // El boton esta siendo presionado
    tone(buzzer, 1000); // Mandamos una señal para que el zumbador reproduzca un pitido de 1KHz...
  }else{
    // El boton NO esta siendo presionado
    noTone(buzzer);     // Paramos el zumbador
  }
  
}
