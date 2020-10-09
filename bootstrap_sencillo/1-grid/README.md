# Grid System de Bootstrap

Bootstrap utiliza una serie de contenedores, filas y columnas para crear el diseño de la página y alinear el contenido.

El siguiente ejemplo crea tres columnas distribuidas de igual manera usando las clases de bootstrap. Las columnas son centradas en la pagina a traves del contenedor padre con la clase `.container`.  Las paginas estarán compuestas por filas `.row` en las que maquetaremos el contenido por columnas `.col`.

```html
<div class="container">
  <div class="row">
    <div class="col-sm">
      One of three columns
    </div>
    <div class="col-sm">
      One of three columns
    </div>
    <div class="col-sm">
      One of three columns
    </div>
  </div>
</div>
```

El sistema que se sigue es de doce columnas, donde si mas de 12 son puestas en una única fila, estas extra serán puestas en una nueva linea.

Para determinar el tamaño de las columnas simplemente tendremos que especificarlo a través de las clases `.col-ancho`. Uno de los potenciales de boostrap viene con las opciones de su grid. Al crear este podemos especifiar en las columnas el ancho de las mismas para tamaños de pantalla pequeños, grandes, medianos... ([info](https://getbootstrap.com/docs/4.5/layout/grid/#grid-options)) Esto se hace a través de las clases `.col-`, `.col-sm`, `.col-md`, `.col-lg`, `.col-xl`. A continuación podemos definir cuantas columnas ocupar, por ejemplo `.col-sm-6`, ocupando 6 columnas en dispositivos pequeños y en adelante.

Disponemos además de ciertas clases para manejar el [alineamiento](https://getbootstrap.com/docs/4.5/layout/grid/#alignment) y otras caracteristicas interesantes. La documentación general del grid puede ser consultada [aquí](https://getbootstrap.com/docs/4.5/layout/grid/).

Mirar el ejemplo base y como se importa bootstrap.


### Offsetting

Podemos desplazar columnas y ordenarlas a nuestro gusto utilizando offsets. Estos offsets llenaran el número de columnas que deseemos con espacios en blanco y nos permitiran desplazar y maquetar como queramos nuestros contenedores. Se añaden a traves de la clase `.offset-` pudiendo especificar en cual tamaño de pantalla y cuantos espacios dejar, por ejemplo `.offset-md-3` dejará 3 espacios de columna en dispositivos md y superiores. Estos offsets los podemos introducir junto al div que contiene la columna con información sin tener que crear un div para estos vacio `<div class="col-md-4 offset-md-4">.col-md-4 .offset-md-4</div>`.

#### Mini Ejercicio

  - Crear una pagina donde tengamos dos columnas. Cada columna tendra [texto](https://www.lipsum.com/) y un color de fondo diferente. Estas columnas ocuparan equitativamente el ancho de la pantalla en dispositivos grandes (md y en adelante), y toda la pantalla cada uno en dispositivos menores.
  - Crear una pagina con una única columna con algo de [texto](https://www.lipsum.com/) y color de fondo. La columna estará centrada y ocupara 6 columnas del grid.