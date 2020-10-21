
int led = 3;

void setup()
{
  pinMode(led, OUTPUT);     //Establecemos el Pin3 como salida
}
void loop()
{
  digitalWrite(led, HIGH);   // Apagamos el led
  delay(2000);
  digitalWrite(led, LOW);    // Prendemos el led
  delay(2000);
}
