from flask import Flask
# Para ser capaces de cargar las vistas necesitamos importar 'tempaltes'
from flask import render_template

# Para poder utilizar las sessiones debemos importar...
from flask import session, escape

# Para poder redireccionar y mandar mensajes flash...
from flask import redirect, url_for, flash

# Necesitamos importar 'request' para identificar el tipo de peticion (GET o POST)
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

# Para utilizar nuestras bases de datos basadas en SQl instalamos flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

import os

# Con os.path.abspath(os.getcwd()) tomamos la ruta absoluta de nuestro entorno de trabajo actual (pwd)
# PODEMOS ACCEDER A NUESTRA BASE DE DATOS A TRAVES DE CONSOLA -> sqlite3 database.db
# Alli si posteriormente escribimos .schema nos muestra el esquema de la DB y podemos hacer operaciones
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

# Instanciamos nuestra aplicacion creando un objeto de flask
app = Flask(__name__)

# DEBEMOS CREAR UNA LLAVE SECRETA PARA QUE OTRA GENTE NO PUEDA CAMBIAR EL VALOR DE LAS VARIABLES DE SESSION
app.secret_key = "1234"

# Necesitamos configurar la aplicacion y decirle donde estara nuestra db
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Para que no salgan notificaciones molestas
# Referimos nuestra base de datos pasandole nuestra aplicacion
db = SQLAlchemy(app)

# Vamos a crear a traves de una clase de Python nuestra tabla/esquema en la base de datos
class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Creamos un identificador unico clave primaria
    nombre = db.Column(db.String(50), nullable=False)
    opinion = db.Column(db.String(255), nullable=False)
    puntuacion = db.Column(db.Integer(), nullable=False)
    telefono = db.Column(db.Integer(), nullable=False)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/agregar_review", methods=["GET", "POST"])
def agregar_review():
    if request.method=="POST": # Si venimos de hacer submit en un formulario
        # Podemos acceder a los valores de lo que nos llega del formulario a traves
        # de request con request.form[input_form_name]
        # Creamos un registro para añadirlo a la base de datos
        new_review = Reviews(
            nombre=request.form["nombre"], telefono=request.form["telefono"], 
            opinion=request.form["opinion"], puntuacion=int(request.form["puntuacion"])
        )
        db.session.add(new_review)
        db.session.commit()

        flash("Valoración almacenada con exito", "success") # Mandamos el mensaje a la redireccion
        return redirect(url_for("index"))

    # Si no accedemos al endpoint a traves de GET o POST es porque se ha accedido de forma
    # 'normal' a traves del navegador y hacemos visible la vista signup.html con el formulario
    return render_template("index.html")


@app.route("/listar/reviews")
def listar_posts():
    todas_reviews =  Reviews.query.order_by(Reviews.id).all() # Seleccionamos todos los posts y ordenamos por id
    # Pasamos a la vista el listado de objetos con todos los posts para que los renderice como quiera
    return render_template("listar_reviews.html", todas_reviews=todas_reviews)


# El inicio del programa es que lance la aplicacion de Flask mediante run()
if __name__ == "__main__":
    db.create_all() # Comrpueba si la db esta creada o no (si no lo esta la crea)
    ## -- Mediante el PARAMETRO de debug=True hacemos que los cambios que realicemos en
    ##      nuestra aplicacion se vean de forma 'inmedianta' en la web, sin tener que parar
    ##      la aplicacion desde la consola y tener que volverla a lanzar
    ## -- Podemos cambiar el puerto de la aplicacion mediante el PARAMETRO port
    app.run(debug=True, port=4242)
