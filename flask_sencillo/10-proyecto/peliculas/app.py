from flask import Flask
# Para ser capaces de cargar las vistas necesitamos importar 'tempaltes'
from flask import render_template

import os

# Instanciamos nuestra aplicacion creando un objeto de flask
app = Flask(__name__)

# DEBEMOS CREAR UNA LLAVE SECRETA PARA QUE OTRA GENTE NO PUEDA CAMBIAR EL VALOR DE LAS VARIABLES DE SESSION
app.secret_key = "1234"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Para que no salgan notificaciones molestas


@app.route("/")
def index():
    return render_template("index.html")


# El inicio del programa es que lance la aplicacion de Flask mediante run()
if __name__ == "__main__":
    ## -- Mediante el PARAMETRO de debug=True hacemos que los cambios que realicemos en
    ##      nuestra aplicacion se vean de forma 'inmedianta' en la web, sin tener que parar
    ##      la aplicacion desde la consola y tener que volverla a lanzar
    ## -- Podemos cambiar el puerto de la aplicacion mediante el PARAMETRO port
    app.run(debug=True, port=4242)
