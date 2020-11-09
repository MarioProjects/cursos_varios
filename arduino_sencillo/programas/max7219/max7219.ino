
#include "LedControlMS.h"
#define NumeroMatrices 1     // Indicamos cuántas matrices vamos a utilizar, 1

LedControl lc=LedControl(12,11,10, NumeroMatrices);

void setup()
   {
      for (int i=0; i< NumeroMatrices ; i++)
        {
          lc.shutdown(i,false);    // Despertar a la matriz
          lc.setIntensity(i,8);    // Intensidad a 8
          lc.clearDisplay(i);      // Borrar la matriz
        }
   }

void loop()
   {
      lc.writeString(0,"HOLA");
      delay(1000);
   }
 
