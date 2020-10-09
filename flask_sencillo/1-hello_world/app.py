# Importamos la libreria de flask
from flask import Flask

# Instanciamos nuestra aplicacion creando un objeto de flask
app = Flask(__name__)

# Creamos un decorador de ruta que espera una direccion que sera 
# a la que accedamos a traves del navegador para llegar a la funcion que
# tiene vinculada el decorador, en este caso index() mediante "/"
@app.route("/")
def index():
    return "Hello world!"

# El inicio del programa es que lance la aplicacion de Flask mediante run()
if __name__ == "__main__":
    ## -- Mediante el PARAMETRO de debug=True hacemos que los cambios que realicemos en
    ##      nuestra aplicacion se vean de forma 'inmedianta' en la web, sin tener que parar 
    ##      la aplicacion desde la consola y tener que volverla a lanzar
    ## -- Podemos cambiar el puerto de la aplicacion mediante el PARAMETRO port
    app.run(debug=True, port=4242)
