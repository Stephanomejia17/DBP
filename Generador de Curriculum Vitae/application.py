from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if not session.get("notes"):
        session["notes"] = []
    if request.method == "POST":
        username = request.form.get("nombres")
        password = request.form.get("apellidos")
        
        session["notes"].append(username)
        session["notes"].append(password)
        

    return render_template("index.html", notes=session["notes"])

@app.route("/register", methods=["GET", "POST"])
def register():
    if not session.get("data"):
        session["data"] = []
    if request.method == "POST":
        correo = request.form.get("correo")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        session["notes"].append(correo)
        session["notes"].append(username)
        session["notes"].append(password1)
        session["notes"].append(password2)

    return render_template("register.html", notes=session["notes"])

@app.route("/cuestionario", methods=["GET", "POST"])
def cuestionario():
    if not session.get("data"):
        session["data"] = []
    if request.method == "POST":
        fullname = request.form.get("fullname")
        profesion = request.form.get("profesion")
        correo = request.form.get("correo")
        number = request.form.get("number")
        estudios = request.form.get("estudios")
        habilidades = request.form.get("habilidades")
        presentacion = request.form.get("presentacion")
        experiencia = request.form.get("experiencia")
        
        session["notes"].append(fullname)
        session["notes"].append(profesion)
        session["notes"].append(correo)
        session["notes"].append(number)
        session["notes"].append(estudios)
        session["notes"].append(habilidades)
        session["notes"].append(presentacion)
        session["notes"].append(experiencia)

    return render_template("cuestionario.html", notes=session["notes"])


@app.route("/condiciones")
def condiciones():
    return render_template("condiciones.html")

@app.route("/curriculums")
def curriculums():
    return render_template("curriculums.html")
@app.route("/generador")
def generador():
    return render_template("generador.html")
@app.route("/plantilla1")
def plantilla1():
    return render_template("plantilla1.html")