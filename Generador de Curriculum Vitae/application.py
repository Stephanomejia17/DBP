from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)
app.secret_key = "abcd1234"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        session['user'] = username
        return redirect(url_for('cuestionario'))
    else:
        return "bad"

@app.route('/cuestionario')
def cuestionario():

    if 'user' in session:
        fullname = request.form['fullname']
        profesion = request.form['profesion']
        correo = request.form['correo']
        number = request.form['number']
        estudios = request.form['estudios']
        habilidades = request.form['habilidades']
        presentacion = request.form['presentacion']
        experiencia = request.form['experiencia']
        return render_template("cuestionario.html")
    else:
        return "No tiene permisos para acceder"

@app.route('/logout')
def logout():

    if 'user' in session:
        session.clear()
        return redirect(url_for('login'))
    
if __name__ == "__main__":
    app.run(debug=True)

    

@app.route("/register", methods=["POST"])
def register():
    correo = request.form['correo']
    username = request.form['username']
    password1 = request.form['password1']
    
    return render_template("register.html")


    


@app.route("/condiciones", methods=["POST"])
def condiciones():
    return render_template("condiciones.html")

@app.route("/curriculums", methods=["GET","POST"])
def curriculums():
    return render_template("curriculums.html")
@app.route("/generador", methods=["GET","POST"])
def generador():
    return render_template("generador.html")
@app.route("/plantilla1", methods=["GET","POST"])
def plantilla1():
    return render_template("plantilla1.html")