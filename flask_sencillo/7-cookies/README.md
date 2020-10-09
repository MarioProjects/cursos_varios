# Cookies en Flask

Una cookie es como una variable que se almacena y es accesible una vez creada desde todas las paginas. Es parecido a una variable de session, nos sirve para guardar informacion como preferencias del usuario. Para que cuando vuelva a entrar a la pagina en un futuro ya las sepamos (idioma, tema...).

Las crearemos y trabajaremos con ellas a través de `make_responese`, `set_cookie` y el objeto request.

Para ejecutar el codigo únicamente deberemos llamar: `python app.py`

### ¿Qué son las cookies?
Una cookie es un archivo creado por un sitio web que contiene pequeñas cantidades de datos y que se envían entre un emisor y un receptor. En el caso de Internet el emisor sería el servidor donde está alojada la página web y el receptor es el navegador que usas para visitar cualquier página web.

Su propósito principal es identificar al usuario almacenando su historial de actividad en un sitio web específico, de manera que se le pueda ofrecer el contenido más apropiado según sus hábitos. Esto quiere decir que cada vez que se visita una página web por primera vez, se guarda una cookie en el navegador con un poco de información. Luego, cuando se visita nuevamente la misma página, el servidor pide la misma cookie para arreglar la configuración del sitio y hacer la visita del usuario tan personalizada como sea posible.

Estas cookies pueden tener una finalidad simple, como saber cuándo fue la última vez que el usuario entró a cierta página web; o algo más importante como es guardar todos los artículos puestos en el carrito de compras de una tienda, una acción que se va guardando en tiempo real.


