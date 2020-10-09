from flask import Flask

# Instanciamos nuestra aplicacion creando un objeto de flask
app = Flask(__name__)

# Creamos un decorador de ruta que espera una direccion que sera 
# a la que accedamos a traves del navegador para llegar a la funcion que
# tiene vinculada el decorador, en este caso index()
@app.route("/")
def index():
    return "Hello world yeah!"

# Vamos a crear una ruta que sera 'hola'
@app.route("/hola") # Para acceder a la ruta unicamente ponermos localhost:puerto/hola
def hola(): # Normalmente a la funcion se le suele llamar relacionado con la ruta
    return "Hola."

# Podemos manejar variables en la barra de direcciones
# Para definirlas unicamente debemos declararlas entre dos signos '<tipo:variable>'
# PODEMOS UTILIZAR DOBLE DECORADORES PARA ASI SER CAPACES DE ESTABLECER VALORES POR DEFECTO A LAS VARIABLES
@app.route("/user/") # Accederiamos como localhost:puerto/user/ devolviendo el valor por defecto de 'username'
@app.route("/user/<string:username>") # Accederiamos como localhost:puerto/user/username
def user(username="Mario"): # La funcion ahora recibe la variable que declaramos
    return f"Hola {username}"

# Tambien contamos con otro tipo de variables: int, float....
@app.route("/numero/<int:n>")
def numero(n):
    return f"Número: {n}"

# Tambien podemos pasar mas de una variabl, pudiendo acceder como 
# localhost:puerto/user/miId/name
@app.route("/user/<int:id>/<string:name>")
def identification(id, name):
    return f"Hola {id} ({name})"
    

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"{n1} + {n2} = {n1+n2}"
    

# El inicio del programa es que lance la aplicacion de Flask mediante run()
if __name__ == "__main__":
    ## -- Mediante el PARAMETRO de debug=True hacemos que los cambios que realicemos en
    ##      nuestra aplicacion se vean de forma 'inmedianta' en la web, sin tener que parar 
    ##      la aplicacion desde la consola y tener que volverla a lanzar
    ## -- Podemos cambiar el puerto de la aplicacion mediante el PARAMETRO port
    app.run(debug=True, port=4242)
