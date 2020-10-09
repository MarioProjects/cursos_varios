from flask import Flask
# Para ser capaces de cargar las vistas necesitamos importar 'tempaltes'
from flask import render_template

# Para utilizar nuestras bases de datos basadas en SQl instalamos flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

import os

# Con os.path.abspath(os.getcwd()) tomamos la ruta absoluta de nuestro entorno de trabajo actual (pwd)
# PODEMOS ACCEDER A NUESTRA BASE DE DATOS A TRAVES DE CONSOLA -> sqlite3 database.db
# Alli si posteriormente escribimos .schema nos muestra el esquema de la DB y podemos hacer operaciones
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

# Instanciamos nuestra aplicacion creando un objeto de flask
app = Flask(__name__)
# Necesitamos configurar la aplicacion y decirle donde estara nuestra db
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Para que no salgan notificaciones molestas

# Referimos nuestra base de datos pasandole nuestra aplicacion
db = SQLAlchemy(app)

# Podemos crear nuestra base de datos a partir de clases de Python
class Posts(db.Model): # Creamos una tabla Posts
    id = db.Column(db.Integer, primary_key=True) # id es un entero y sera la clave primaria
    titulo = db.Column(db.String(50)) # Indicamos que titulo es de tipo string con maximo 50 caracteres


# Creamos un decorador de ruta que espera una direccion que sera
# a la que accedamos a traves del navegador para llegar a la funcion que
# tiene vinculada el decorador, en este caso index()
@app.route("/")
def index():
    # La funcion render_template va a la carpeta de 'templates' y busca para renderizar
    # El archivo que le indicamos, en este caso en index.html
    # Podemos compartir valroes de variables de Python entre este y nuestros ficheros
    # de forma sencilla al pasarselos. Dentro de index.html podemos acceder a la variable {{ titulo }}
    titulo_web = "SQLite test!"
    return render_template("index.html", titulo=titulo_web)


## Vamos a crear una ruta para insertar un registro en la tabla de Posts
@app.route("/insert/default")
def insert_default():
    new_post = Posts(titulo="Default titulo") # Creamos una entrada a partir de su constructor
    db.session.add(new_post) # Añadimos el nuevo post
    db.session.commit() # Confirmamos la accion de añadir el post
    return "El post por defecto ha sido creado" # Devolvemos algo para el cliente


## A continuacion vamos a hacer una consulta sobre nuestra tabla Posts
@app.route("/select/default")
def select_default():
    first_post = Posts.query.filter_by(id=1).first()
    if first_post is None:
        return "No existen posts que cumplan los requisitos!"
    return "El titulo del primer post es: " + str(first_post.titulo)


## Podemos actualizar un objeto a traves de una consulta sobre nuestra tabla Posts
@app.route("/update/default")
def update_default():
    first_post = Posts.query.filter_by(id=1).first()
    first_post.titulo = "Un titulo inventado"
    db.session.commit()
    return "Actualizado el primer post!"


## Podemos eliminar un objeto a traves de una consulta sobre nuestra tabla Posts
@app.route("/remove/default")
def remove_default():
    first_post = Posts.query.filter_by(id=1).first()
    db.session.delete(first_post)
    db.session.commit()
    return "Borrado el primer post!"


# El inicio del programa es que lance la aplicacion de Flask mediante run()
if __name__ == "__main__":
    db.create_all() # Comrpueba si la db esta creada o no (si no lo esta la crea)
    ## -- Mediante el PARAMETRO de debug=True hacemos que los cambios que realicemos en
    ##      nuestra aplicacion se vean de forma 'inmedianta' en la web, sin tener que parar
    ##      la aplicacion desde la consola y tener que volverla a lanzar
    ## -- Podemos cambiar el puerto de la aplicacion mediante el PARAMETRO port
    app.run(debug=True, port=4242)
