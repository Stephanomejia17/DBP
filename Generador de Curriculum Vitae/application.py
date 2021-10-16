from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    username = request.form.get("nombres")
    password = request.form.get("apellidos")

    return render_template("index.html", notes=session["notes"])

@app.route("/register", methods=["GET", "POST"])
def register():
    correo = request.form.get("correo")
    username = request.form.get("username")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")
    
    return render_template("register.html", notes=session["notes"])

@app.route("/cuestionario", methods=["GET", "POST"])
def cuestionario():
    
    fullname = request.form.get("fullname")
    profesion = request.form.get("profesion")
    correo = request.form.get("correo")
    number = request.form.get("number")
    estudios = request.form.get("estudios")
    habilidades = request.form.get("habilidades")
    presentacion = request.form.get("presentacion")
    experiencia = request.form.get("experiencia")

    return render_template("cuestionario.html", notes=session["notes"])


@app.route("/condiciones", methods=["GET", "POST"])
def condiciones():
    return render_template("condiciones.html")

@app.route("/curriculums", methods=["GET", "POST"])
def curriculums():
    return render_template("curriculums.html")
@app.route("/generador", methods=["GET", "POST"])
def generador():
    return render_template("generador.html")
@app.route("/plantilla1", methods=["GET", "POST"])
def plantilla1():
    return render_template("plantilla1.html")