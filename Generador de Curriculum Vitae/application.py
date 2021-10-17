from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template('login.html')
    
@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        return render_template("cuestionario.html")
    else:
        return "bad request"
    

@app.route("/register", methods=["POST"])
def register():
    correo = request.form['correo']
    username = request.form['username']
    password1 = request.form['password1']
    password2 = request.form['password2']
    
    return render_template("register.html")

@app.route("/cuestionario", methods=["POST"])
def cuestionario():
    
    fullname = request.form['fullname']
    profesion = request.form['profesion']
    correo = request.form['correo']
    number = request.form['number']
    estudios = request.form['estudios']
    habilidades = request.form['habilidades']
    presentacion = request.form['presentacion']
    experiencia = request.form['experiencia']

    return render_template("cuestionario.html")


@app.route("/condiciones", methods=[ "POST"])
def condiciones():
    return render_template("condiciones.html")

@app.route("/curriculums", methods=["POST"])
def curriculums():
    return render_template("curriculums.html")
@app.route("/generador", methods=["POST"])
def generador():
    return render_template("generador.html")
@app.route("/plantilla1", methods=["POST"])
def plantilla1():
    return render_template("plantilla1.html")