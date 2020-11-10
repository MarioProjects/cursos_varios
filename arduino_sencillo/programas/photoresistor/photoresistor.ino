void setup() {
  Serial.begin(9600);
}


void loop() {
  int value = analogRead(A0);
  Serial.println("Luz: ");
  Serial.println(value);
  delay(750);
}
