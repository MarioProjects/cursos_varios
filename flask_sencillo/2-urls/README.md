# Urls en Flask

A traves de los decoradores que habíamos visto, podemos crear diferentes rutas en función de nuestras necesidades, y es que mediante las rutas podemos pasar argumentos que manejaremos en el servidor a conveniencia. Los tipos de argumentos/variables que podemos instanciar son:

|  Tipo  |              Definicion             |
|:------:|:-----------------------------------:|
| string | (default) Acepta un texto sin slash |
|   int  |       Acepta positivos enteros      |
|  float |       Acepta positivos reales       |
|  path  |    Como string pero acepta slash    |
|  uuid  |         Acepta strings UUID         |

Se indican como `<tipo:NOMBRE_VARIABLE>` y podemos requerir mas de uno y dar valores por defecto.

Para ejecutar el codigo únicamente deberemos llamar: `python app.py`

### Mini Ejercicio

   - Crear un ruta llamada '/cuadrado' a la que podamos pasarle un numero entero y devolvamos un su cuadrado.

   - ¿Porque da error si tratamos de acceder a la ruta 'http://localhost:4242/suma/1/2'? (Pista: Mirar el tipo de dato requerido)