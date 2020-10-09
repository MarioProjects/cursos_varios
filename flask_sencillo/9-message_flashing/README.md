# Mensajes Flash en Flask

Hay ocasiones en que deseamos mandar un mensaje al usuario o que el servidor nos devuelva una respuesta sin tener que redireccionar o renderizar un template de nuevo. Para ello lo que haremos entonces será utilizar mensajes flash. En esta unidad hemos añadido dos mensajes flash en `signup` y `login`. El primer caso mandamos el mansaje flash y redirigimos al entrypoint de login donde se mostrará dicho mensaje. En el segundo caso se cargará sobre la misma pagina.

Podemos dotar a estos mensajes con una categoria para tratarlos de una forma u otra. Posteriormente, con jinja podemos recoger estos mensajes y su categoria y trabajar como deseemos (mirar base.html).

Para ejecutar el codigo únicamente deberemos llamar: `python app.py`
