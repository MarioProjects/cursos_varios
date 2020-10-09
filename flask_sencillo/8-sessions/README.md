# Sesiones en Flask

En esta unidad vamos a ver como trabajar con sesiones en el autenticado y manejo de los datos de un usuario registrado/logueado. Principalmente al loguearnos creamos una variable de session que almacena el usuario y al hacer logout la destruimos. Podriamos ir mirando en cada endpoint si tenemos el usuario en la session y trabajar en función de esto.

Las sessions en flask expiran una vez el buscador se cierra. Para acceder mediante jinja2 a las variables de session, estas se almacenan en el objeto session, por lo tanto `{{session['mi_variable']}}`.

Para ejecutar el codigo únicamente deberemos llamar: `python app.py`

### Diferencias con Cookies

La diferencia entre session y cookies La gran diferencia es que las sesiones se mantienen por un período de tiempo determinado (por ejemplo, una hora), en el servidor, o bien, hasta que se cierre el navegador; mientras que las cookies, siempre que sean aceptadas por el navegador, se mantienen en el cliente (navegador del usuario), hasta que no sea eliminada manualmente por el mismo.

### Mini Ejercicio

  - Rediriguir del signup al indice si el usuario ya esta logueado.
  - Eliminar el boton de registrarse si el usuario esta logueado. (Pista: utilizar if con Jinja [documentación](https://jinja.palletsprojects.com/en/2.10.x/templates/)).