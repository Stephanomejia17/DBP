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
        nombre = request.form.get("nombres")
        apellidos = request.form.get("apellidos")
        correo = request.form.get("correo")
        number = request.form.get("number")
        estudios = request.form.get("estudios")
        habilidades = request.form.get("habilities")
        presentacion= request.form.get("presentacion")
        experiencia = request.form.get("experiencia")
        session["notes"].append(nombre)
        session["notes"].append(apellidos)
        session["notes"].append(correo)
        session["notes"].append(number)
        session["notes"].append(estudios)
        session["notes"].append(habilidades)
        session["notes"].append(presentacion)
        session["notes"].append(experiencia)

    return render_template("index.html", notes=session["notes"])

@app.route("/condiciones")
def condiciones():
    return render_template("condiciones.html")
