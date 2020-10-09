from flask import Flask
# Para ser capaces de cargar las vistas necesitamos importar 'tempaltes'
from flask import render_template

# Instanciamos nuestra aplicacion creando un objeto de flask
app = Flask(__name__)

# Creamos un decorador de ruta que espera una direccion que sera 
# a la que accedamos a traves del navegador para llegar a la funcion que
# tiene vinculada el decorador, en este caso index()
@app.route("/")
def index():
    # La funcion render_template va a la carpeta de 'templates' y busca para renderizar
    # El archivo que le indicamos, en este caso en index.html

    # Podemos compartir valroes de variables de Python entre este y nuestros ficheros 
    # de forma sencilla al pasarselos. Dentro de index.html podemos acceder a la variable {{ titulo }}
    titulo_web = "Home!"
    # Tambien podemos pasar listas y iterar sobre ellas (mas en index.html)
    lista = ["Valor1", "Valor2", "Valor3"]
    return render_template("index.html", titulo=titulo_web, lista=lista)


# El inicio del programa es que lance la aplicacion de Flask mediante run()
if __name__ == "__main__":
    ## -- Mediante el PARAMETRO de debug=True hacemos que los cambios que realicemos en
    ##      nuestra aplicacion se vean de forma 'inmedianta' en la web, sin tener que parar 
    ##      la aplicacion desde la consola y tener que volverla a lanzar
    ## -- Podemos cambiar el puerto de la aplicacion mediante el PARAMETRO port
    app.run(debug=True, port=4242)
