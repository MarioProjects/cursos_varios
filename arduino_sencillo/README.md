# Curso de Arduino

## 1. Arduino y sistema basados en hardware y software libre

Arduino es uno de los tipos de las placas más populares del mundo maker, pero que a diferencia de la Raspberry Pi no cuenta con un único modelo, sino que ofrece unas bases de hardware abierto para que otros fabricantes puedan crear sus propias placas.

El proyecto **nació en 2003**, cuando varios estudiantes del Instituto de Diseño Interactivo de Ivrea, Italia, con el fin de facilitar el acceso y uso de la electrónico y programación. Lo hicieron para que los estudiantes de electrónica tuviesen una alternativa más económica a las populares BASIC Stamp, unas placas que por aquel entonces valían más de cien dólares, y que no todos se podían permitir.

El resultado fue Arduino, una placa con todos los elementos necesarios para conectar periféricos a las entradas y salidas de un microcontrolador, y que puede ser programada tanto en Windows como macOS y GNU/Linux. Un proyecto que promueve la filosofía 'learning by doing', que viene a querer decir que la mejor manera de aprender es cacharreando.

Arduino es una plataforma de creación de electrónica de **código abierto**, la cual está basada en **hardware y software libre**, flexible y fácil de utilizar para los creadores y desarrolladores. Esta plataforma permite crear diferentes tipos de microordenadores de una sola placa a los que la comunidad de creadores puede darles diferentes tipos de uso.

Para poder entender este concepto, primero vas a tener que entender los conceptos de hardware libre y el software libre. **El hardware** libre son los dispositivos cuyas especificaciones y diagramas son de acceso público, de manera que cualquiera puede replicarlos. Esto quiere decir que Arduino ofrece las bases para que cualquier otra persona o empresa pueda crear sus propias placas, pudiendo ser diferentes entre ellas pero igualmente funcionales al partir de la misma base.

**El software libre** son los programas informáticos cuyo código es accesible por cualquiera para que quien quiera pueda utilizarlo y modificarlo. Arduino ofrece la plataforma Arduino IDE (Entorno de Desarrollo Integrado), que es un entorno de programación con el que cualquiera puede crear aplicaciones para las placas Arduino, de manera que se les puede dar todo tipo de utilidades.

#### Cómo funciona Arduino

El Arduino es una placa basada en un microcontrolador ATMEL. Los microcontroladores son circuitos integrados en los que se pueden grabar instrucciones, las cuales las escribes con el lenguaje de programación que puedes utilizar en el entorno Arduino IDE. Estas instrucciones permiten crear programas que interactúan con los circuitos de la placa.

El microcontrolador de Arduino posee lo que se llama una interfaz de entrada, que es una conexión en la que podemos conectar en la placa diferentes tipos de periféricos. La información de estos periféricos que conectes se trasladará al microcontrolador, el cual se encargará de procesar los datos que le lleguen a través de ellos.

El tipo de periféricos que puedas utilizar para enviar datos al microcontrolador depende en gran medida de qué uso le estés pensando dar. Pueden ser cámaras para obtener imágenes, teclados para introducir datos, o diferentes tipos de sensores.

También cuenta con una interfaz de salida, que es la que se encarga de llevar la información que se ha procesado en el Arduino a otros periféricos. Estos periféricos pueden ser pantallas o altavoces en los que reproducir los datos procesados, pero también pueden ser otras placas o controladores.

Arduino es un proyecto y no un modelo concreto de placa, lo que quiere decir que compartiendo su diseño básico te puedes encontrar con diferentes tipos de placas. Las hay de varias formas, tamaños y colores para a las necesidades del proyecto en el que estés trabajando, las hay sencillas o con características mejoradas, Arduinos orientados al Internet de las Cosas o la impresión 3D y, por supuesto, dependiendo de estas características te encontrarás con todo tipo de precios.

Además, las placas Arduino también cuentan con otro tipo de componentes llamados Escudos (Shields) o mochilas. Se trata de una especie de placas que se conectan a la placa principal para añadirle una infinidad de funciones, como GPS, relojes en tiempo real, conectividad por radio, pantallas táctiles LCD, placas de desarrollo, y un larguísimo etcétera de elementos. Incluso hay [tiendas](https://www.cetronic.es/sqlcommerce/disenos/plantilla1/seccion/Catalogo.jsp?gclid=CjwKEAjwxruuBRC9lLGslqjs-HISJAAkq21srnMhxnzsJIWwQYBfY91AuEwALyhaKK0Ud4-FeBxkixoC96Xw_wcB&idIdioma=&cPath=1342&idTienda=93) con secciones especializadas en dichos elementos.

#### Proyectos

La enorme flexibilidad y el carácter libre y abierto de Arduino hacen que puedas utilizar este tipo de placas prácticamente para cualquier cosa, desde relojes hasta básculas conectadas, pasando por robots, persianas controladas por voz o tu propia vending machine . En [este artículo](https://www.xataka.com/makers/46-proyectos-makers-para-hacer-verano-arduino-raspberry-pi) tienes varias decenas de ejemplos.

## 2. Entorno de programación y configuración

### Instalación

Debemos acceder a la página de de descarga de Software para la instalación de [Arduino](https://www.arduino.cc/en/Main/Software). Desde aquí decargaremos la versión que sea adecuada para nuestro sistema operativo.

#### Posibles problemas

**Ubuntu**. Si tenemos problemas a la hora de compilar y subir a nuestra placa el codigo generado por temas de permisos: `sudo chmod a+rw /dev/ttyACM0`.

## 3. Sensores digitales. Entradas y salidas digitales.

## 4. Sensores analógicos. Entradas y salidas analógicas.

## 5. Comunicaciones electrónica-sensores. Comunicación serie, bluetooth

## 6. Comunicación electrónica-sensores. Comunicación wifi ESP8266.
https://www.luisllamas.es/arduino-wifi-esp8266-esp01/