# Jinja2 en Flask

Jinja 2 es un motor de plantillas para Python, lo que significa que le permite al desarrollador producir páginas web, que contienen, por ejemplo, código html base y marcadores de posición para que Jinja 2 los llene

Jinja es simple. Tienes una plantilla con un montón de agujeros en ella. Luego, le pide al motor, Flask, que llene la plantilla con los valores que le da en el tiempo de ejecución, y se le devuelve la respuesta, en forma de un documento html, listo para ser enviado al usuario. También tiene posibilidades más avanzadas, como aplicar un filtro a una variable, para mostrar, por ejemplo, un tiempo de lectura basado en la página de un artículo para un blog

Cosas interesantes en esta unidad:
  - En nuestro archivo 'templates/index.html' podemos ver como podemos heredar trozos de codigo de otros ficheros, 'tempaltes'base.html en este caso, a traves de 'extends' y 'block/endblock'. Con esto podemos unificar el tema de diferentes paginas que compartan un mismo header, footer u otros elementos.
  - Por otra parte podemos ver como a traves de nuestra ruta/decorador podemos mandar información a la vista y que esta la renderice. En el ejemplo renderizamos un string mediante el uso de dobles corchetes y una lista iterando sobre sus elementos.


Para ejecutar el codigo únicamente deberemos llamar: `python app.py`


### Mini Ejercicio

  - Crear un servicio ("/palindromo") que reciba en la ruta un string y compruebe si este es un palindromo (palabra o frase que se lee igual en un sentido que en otro, como Ana). Devolver la palabra y si este es o no un palindromo.