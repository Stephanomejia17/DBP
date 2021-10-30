from flask import Flask, redirect, session,render_template, request, url_for

app = Flask(__name__)
app.secret_key = "abcd1234" #encriptar inicio de sesion

@app.route('/')
def index():
    return render_template("login.html")
@app.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        session['user1'] = email
        session['pass'] = password

        return redirect(url_for('cuestionario'))
    else:
        return "bad request"

@app.route('/cuestionario')
def cuestionario():
    if 'user1' in session and 'pass' in session:
        return render_template("cuestionario.html")
    else:
        return redirect(url_for('No_Register'))
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
    
@app.route("/No_Register", methods=["POST"])
def No_Register():
    return render_template("No_Register.html")

@app.route("/register", methods=["POST"])
def register():
    return render_template("register.html")

@app.route("/condiciones", methods=["POST"])
def condiciones():
    return render_template("condiciones.html")

@app.route("/curriculums", methods=["POST"])
def curriculums():
    return render_template("curriculums.html")

@app.route("/plantilla1", methods=["POST"])
def plantilla1():
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    profesion = request.form.get("profesion")
    correo = request.form.get("correo")
    estudios = request.form.get("estudios")
    habilidades = request.form.get("habilidades")
    presentacion = request.form.get("presentacion")
    experiencia = request.form.get("experiencia")
    logros = request.form.get("logros")
    info = request.form.get("info")


    return render_template("plantilla1.html",nombre=nombre,apellido=apellido,profesion=profesion,correo=correo,estudios=estudios,habilidades=habilidades,presentacion=presentacion,experiencia=experiencia,logros=logros,info=info)
@app.route("/plantilla2", methods=["POST"])
def plantilla2():
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    profesion = request.form.get("profesion")
    correo = request.form.get("correo")
    estudios = request.form.get("estudios")
    habilidades = request.form.get("habilidades")
    presentacion = request.form.get("presentacion")
    experiencia = request.form.get("experiencia")
    logros = request.form.get("logros")
    info = request.form.get("info")


    return render_template("plantilla2.html",nombre=nombre,apellido=apellido,profesion=profesion,correo=correo,estudios=estudios,habilidades=habilidades,presentacion=presentacion,experiencia=experiencia,logros=logros,info=info)

@app.route("/generador", methods=["POST"])
def generador():
    if True:
        return redirect(url_for('plantilla1'))
    else:
        return redirect(url_for('plantilla2'))



if __name__ == "__main__":
    app.run(debug=True)
