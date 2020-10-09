# Base de datos en Flask

En esta unidad vamos a ver como trabajar con una pequeña base de datos creada con SQL. Para ello necesitaremos el paquete de `flask_sqlalchemy`. Referimos en nuestra app donde queremos crear la base de datos y Flask se encargara de mirar si esta creada y si no es así crearla. 

A continuación creamos un objeto para trabajar con la base de datos que tomara la app de flask y así poder crear un vinculo y que estas interactuen. Creamos una tabla en nuestra base de datos a la que llamaremos Posts. Esta tabla estará compuesta por dos campos, el id y el titulo del post. Podemos asignar ciertos atributos a estos campos como que sean clave primaria o el tipo de datos y longitud.

Para insertar entradas en la tabla crearemos un post a partir del constructor de Posts y mediant `add(entrada)` y `commit()` lo añadiremos a nuestra base de datos. 

Podemos realizar consultas/queries sobre la base de datos y filtrar facilmente.

Mas información sobre queries en flask [aqui](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/).

Para ejecutar el codigo únicamente deberemos llamar: `python app.py`


### Mini Ejercicio

  - Hacer una ruta para listar todos los posts
  - Añadir un boton de borrado junto a los posts y que borre dicho post
  - (Opcional) - Crear ruta para modificar un post donde el titulo esta en un input [(pista)](https://stackoverflow.com/a/11566296)