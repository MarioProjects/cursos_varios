#include <Keypad.h>

const byte ROWS = 4; //4 filas
const byte COLS = 4; //4 columnas
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte rowPins[ROWS] = {5, 4, 3, 2}; // conexion de los pines de las filas keypad - arduino
byte colPins[COLS] = {9, 8, 7, 6}; // conexion de los pines de las columnas keypad - arduino

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

void setup(){
   Serial.begin(9600);
}
  
void loop(){
  char key = keypad.getKey();
  if (key){
    Serial.println(key);
  }
}
