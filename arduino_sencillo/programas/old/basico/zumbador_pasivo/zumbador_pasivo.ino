const int buzzer = 9; //Ponemos el zumbador en el pin 9


void setup(){
 
  pinMode(buzzer, OUTPUT); // Indicamos que el pin del zumbador debe ser tratado como una salida

}

void loop(){
 
  tone(buzzer, 1000, 500); // Mandamos una señal para que el zumbador reproduzca un pitido de 1KHz...
  delay(1000);        // esperamos 1 segundo
  noTone(buzzer);     // Paramos el zumbador
  delay(1000);        // esperamos 1 segundo
  
}
