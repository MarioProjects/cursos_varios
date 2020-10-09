from flask import Flask
# Para ser capaces de cargar las vistas necesitamos importar 'tempaltes'
from flask import render_template

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

# Necesitamos configurar la aplicacion y decirle donde estara nuestra db
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Para que no salgan notificaciones molestas
# Referimos nuestra base de datos pasandole nuestra aplicacion
db = SQLAlchemy(app)

# Vamos a crear a traves de una clase de Python nuestra tabla/esquema en la base de datos
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Creamos un identificador unico clave primaria
    # Creamos una columna para el nombre de usuario que sea unica (no usernames iguales y que no este vacio/null)
    username = db.Column(db.String(50), unique=True, nullable=False)
    # Algo parecido para el password
    password = db.Column(db.String(80), nullable=False)

@app.route("/")
def index():
    return render_template("index.html")

# Vamos a crear un endpoint que busca un usuario
@app.route("/search", methods=["GET", "POST"])
def search():
    # El formulario envia la informacion por GET y para tomar el valor lo hacemos como sigue
    # Este formulario se encuentra en index.html
    nickname = request.args.get("nickname")
    # Buscamos a ver si existe una entrada con username igual al que nos han indicado
    user = Users.query.filter_by(username=nickname).first()
    if user: # Si existe usuario lo indicamos
        return "The user " + user.username + " is correctly registered."
    return "The user doesn't exist" # No existe el usuario


# Las rutas definidas mediante flask tienen como predeterminado recibir una peticion de tipo GET
# Pero la accion de signup se realiza mediante POST y debemos preprarar nuestra ruta
# Podemos definir diferentes puntos de entrada con el mismo nombre que hagan cosas diferentes
# dependiendo si se llama por GET o POST pero en este caso vamso a aceptar las dos peticiones
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method=="POST": # Si venimos de hacer submit en un formulario
        # Podemos acceder a los valores de lo que nos llega del formulario a traves
        # de request con request.form[input_form_name]
        hashed_pw = generate_password_hash(request.form["password"], method="sha256") # Ciframos el password
        # Creamos un registro para añadirlo a la base de datos
        new_user = Users(username=request.form["username"], password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        # Devolvemos una vista recordad (deberia ser render_template)
        # Aqui nos basta con sacar que ha ido todo bien
        return "You've registered successfully"

    # Si no accedemos al endpoint a traves de GET o POST es porque se ha accedido de forma
    # 'normal' a traves del navegador y hacemos visible la vista signup.html con el formulario
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST": # Si venimos de hacer submit en un formulario
        ## Primero comprobamos que el usuario exista en la base de datos
        user = Users.query.filter_by(username=request.form["username"]).first()
        # SI ha encontrado usuario y el usuario tiene el password como el introducido...
        # Es importante el orden de check_password_hash ya que hace el hash al segundo parametro
        if user and check_password_hash(user.password, request.form["password"]):
            return "You are logged in"
        else: return "Your credentials are invalid"

    return render_template("login.html")

# El inicio del programa es que lance la aplicacion de Flask mediante run()
if __name__ == "__main__":
    db.create_all() # Comrpueba si la db esta creada o no (si no lo esta la crea)
    ## -- Mediante el PARAMETRO de debug=True hacemos que los cambios que realicemos en
    ##      nuestra aplicacion se vean de forma 'inmedianta' en la web, sin tener que parar
    ##      la aplicacion desde la consola y tener que volverla a lanzar
    ## -- Podemos cambiar el puerto de la aplicacion mediante el PARAMETRO port
    app.run(debug=True, port=4242)
