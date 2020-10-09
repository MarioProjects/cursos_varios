from flask import Flask
# Para ser capaces de cargar las vistas necesitamos importar 'tempaltes'
from flask import render_template

# Instanciamos nuestra aplicacion creando un objeto de flask
app = Flask(__name__)

@app.route("/palindromo/<string:palabra>")
def palindromo(palabra):
    es_palindromo = "SI" if palabra.lower() == palabra[::-1].lower() else "NO"
    return render_template("palindromo.html", palabra=palabra, es_palindromo=es_palindromo)

# El inicio del programa es que lance la aplicacion de Flask mediante run()
if __name__ == "__main__":
    ## -- Mediante el PARAMETRO de debug=True hacemos que los cambios que realicemos en
    ##      nuestra aplicacion se vean de forma 'inmedianta' en la web, sin tener que parar 
    ##      la aplicacion desde la consola y tener que volverla a lanzar
    ## -- Podemos cambiar el puerto de la aplicacion mediante el PARAMETRO port
    app.run(debug=True, port=4242)
