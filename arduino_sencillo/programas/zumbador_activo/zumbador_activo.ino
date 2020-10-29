

int zumbador = 12;  // El pin donde estará el zumbador activo

void setup(){
  pinMode(zumbador, OUTPUT);  // Inicializamos el pin del zumbador como salida
}

void loop(){
  digitalWrite(zumbador,HIGH);
  delay(100);  // sonamos durante 100ms
  digitalWrite(zumbador,LOW);
  delay(500);  // silenciamos durante 500ms
}
