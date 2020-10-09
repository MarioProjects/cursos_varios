# Una cookie es como una variable que se almacena y es accesible una vez creada desde todas las paginas
# Es parecido a una variable de session, nos sirve para guardar informacion como preferencias del usuario
# Para que cuando vuelva a entrar a la pagina en un futuro ya las sepamos... Idioma, tema...
from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

# Creamos una ruta que se encargara de crear nuestra cookie
@app.route("/cookie/set")
def set_cookie():
    # Para crear la cookie debemos en primer lugar crear un objeto a partir de make_response()
    # Este toma un render template con la pagina a mostrar
    resp = make_response(render_template("index.html"))
    # A continuacion podemos instanciar nuestra cookie con nombre 'username' y valor 'maparla'
    resp.set_cookie("username", "maparla")
    # Devolvemos el objeto/vista que renderizara index.html y establecera la cookie
    return resp

# Creamos una ruta para leer la cookie creada al acceder a la ruta anterior
@app.route("/cookie/read")
def get_cookie():
    # Tomamos la cookie a traves de request -> cookies y indicamos la cookie a tomar
    # Podemos definir un valor por defecto si no encuentra la cookie, en este caso None
    username = request.cookies.get("username", None)
    if username==None:
        return "La cookie username no existe!"
    # Si encontramos la cooki devolvemos su valor
    return "El valor de la cookie username es: " + username

if __name__ == '__main__':
    app.run(debug=True, port=4242)