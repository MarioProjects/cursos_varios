# Vistas estatic en Flask

Cuando trabajamos con flask necesitaremos poder renderizar sitios web y no devolver simples strings (a no ser que solo utilicemos flask para crear servicios diferentes). Podemos a través de la función `render_template` indicar que deseamos renderizar en una ruta concreta. Esta función funciona con una estructura determinada de carpetas donde tendremos en la carpeta 'static' los recursos que nuestras páginas HTML almacenadas en 'tempaltes' utilizará.

Para ejecutar el codigo únicamente deberemos llamar: `python app.py`
