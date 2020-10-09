# Mini curso de JQuery

JQuery es una librería de JavaScript (JavaScript es un lenguaje de programación muy usado en desarrollo web). Esta librería de código abierto, simplifica la tarea de programar en JavaScript y permite agregar interactividad a un sitio web sin tener conocimientos del lenguaje.

Basados en esta librería, existe una infinita cantidad de plugins (gratis y pagos) creados por desarrolladores de todo el mundo. Estos plugins resuelven situaciones concretas dentro del maquetado de un sitio, por ejemplo: un menú responsive, una galería de fotos, un carrousel de imágenes, un slide, un header que cambia de tamaño, el deslizamiento del scroll al hacer clic en un botón (anclas HTML), la transición entre páginas y miles de efectos más.

Cada plugin tiene un sitio web desde donde se pueden descargar sus archivos, con demos, instrucciones para su implementación, opciones de configuración e información de las licencias. En la web hay cientos de blogs que recopilan y analizan los plugins según sus funcionalidades, reuniendo en un sólo post los links a varios plugins de función similar, lo que facilita mucho la búsqueda.

## Selección con JQuery

JQuery nos permite de forma sencilla seleccionar elementos de nuestra página a traves de diferentes selectores. Una lista completa la podemos consultar [aquí](https://www.w3schools.com/jquery/jquery_ref_selectors.asp).

Entre los selectores mas comúnes enonctramos:

  - Id: Aquel elemento con el id 'element_id' `$("#element_id")`
  - Clase: Aquel o aquellos elementos con la clase 'element_class' `$(".element_class")`
  - Múltiple: Aquellos elementos con la clase 'element_class' o el id 'element_id' `$(".element_class,#element_id")`
  - Elementos: Todos los elementos con la etiqueta 'p' `$("p")`
  
Selección especifica:

   - Primero: ':first', por ejemplo `$("p:first")`
   - último: ':last', por ejemplo `$("p:last")`
   - Pares: ':even', por ejemplo `$("p:even")`
   - Impares:  ':odd', por ejemplo `$("p:odd")`
   
Existen muchos mas selectores como introduciamos.

## Manipulación del DOM

Podemos manipular nuestra página de diferentes formas con JQuery:

  - **prepend(val)**: inserta el contenido especificado como parametro al principio de cada elemento seleccionado (dentro).
  - **append(val)**: inserta el contenido especificado como parametro al final de cada elemento seleccionado (dentro).
  - **before(val)**: inserta el contenido especificado como parametro antes de cada elemento seleccionado (fuera).
  - **after(val)**: inserta el contenido especificado como parametro después de cada elemento seleccionado (fuera).
  - **remove(val)**: elimina todos los elementos seleccionados.
  - **empty(val)**: vacia los elementos seleccionados, elimina los nodos hijo de los elementos seleccionados.
  - **attr(attName, val)**: modifica el atributo de los elementos seleccionados.
  - **css(propName, val)**: modifica el estilo de un elemento, para ello se toma el nombre de la propieda de estilo y el valor deseado.

#### Mini Ejercicios

  - Probar los metodos descritos previamente. Analizar el comportamiento. ¿Que diferencia hay entre prepend y before?
  - Crear una lista simple con 10 elementos. Los elementos pares tendran un color de letra azul, los impares verde.
  
## Eventos

JQuery nos permite reaccionar a una serie de [eventos](https://www.w3schools.com/jquery/jquery_events.asp)

#### Mini Ejercicios

  - Crear una página con un boton y un div vacio con el identificador 'mi_contenedor'. Al hacer click sobre el boton añadir parrafos a 'mi_contenedor' con un texto determinado.
  - Crear una página con un boton que al hacer click cambie el color de la página a un color aleatorio. 

## Animaciones, Efectos y 'this'

Algo interesante y visual para el usuario son las animaciones y efectos:

  - **Fadding**: Podemos desvanecer objetos o que estos aparezcan de forma suave animando su transparencia. Para ello contamos con los [efectos de fading](https://www.w3schools.com/jquery/jquery_fade.asp).
  - **Sliding**: Podemos hacer aparecer objetos o que desaparezcan animando su anchura o altura. Para ello contamos con los [efectos de sliding](https://www.w3schools.com/jquery/jquery_slide.asp).
  - **Animacion general**: En general podemos animar las propiedades del css de nuestros elementos mediante [`animate()`](https://api.jquery.com/animate/). Con esta podriamos conseguir los efectos de sliding y fading, incluso de [forma horizontal](https://stackoverflow.com/questions/596608/slide-right-to-left)

#### Mini Ejercicios

  - Crear varios contenedores con una anchura y altura de 300px. Cada uno de un color diferente. Todos deben tener la misma clase y cuándo hagamos click en alguno, ese y solo ese se desvanecerá.

## Plugins

Existe infinidad de plugins que podemos utilizar y que facilitaran nuestra vida a la vez que dotan de funcionalidad nuestra pagina. [Aqui](https://speckyboy.com/free-jquery-plugins/) hay unos cuantos gratuitos.

#### Mini Ejercicios

  - Un cliente quiere crear un sistema de reservas y el usuario tiene que seleccionar una hora. Probar el plugin de [clockpicker](https://weareoutman.github.io/clockpicker/). [Aquí](https://github.com/weareoutman/clockpicker) también hay opciones.
  
  
## Ajax

Tenemos la documentación [aquí](https://api.jquery.com/jquery.ajax/). Como mejor lo veremos será con un [ejemplo](https://hackersandslackers.com/making-ajax-calls-with-jquery/).

  - [Linkpreview](https://www.linkpreview.net/) Es un API que nos premite obtener previsualizaciones de paginas web de forma gratuita.

HTTP Response Code: 429 = Too many requestjqs / rate limit exceeded

 -  Si recargamos la página, los cards aparecen en un orden diferente... ¿Porque?
 - Ideas de mejora: [spinner](https://getbootstrap.com/docs/4.5/components/spinners/), [alturas](https://brm.io/jquery-match-height/)...