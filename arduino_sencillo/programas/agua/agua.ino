// Pines de los sensores
#define sensorPower 7
#define sensorPin A0

// Value for storing water level
int val = 0;

void setup() {
  // Set D7 as an OUTPUT
  pinMode(sensorPower, OUTPUT);
  
  // Set to LOW so no power flows through the sensor
  digitalWrite(sensorPower, LOW);
  
  Serial.begin(9600);
}

void loop() {
  // Obtenemos el nivel de agua para imprimirlo
  int nivel = readSensor();
  
  Serial.print("Nivel del agua: ");
  Serial.println(nivel);
  
  delay(1000);
}

// Esta funcion la usamos para leer el modulo del agua
int readSensor() {
  digitalWrite(sensorPower, HIGH);   // Turn the sensor ON
  delay(10);                         // wait 10 milliseconds
  val = analogRead(sensorPin);       // Read the analog value form sensor
  digitalWrite(sensorPower, LOW);    // Turn the sensor OFF
  return val;                        // send current reading
}
