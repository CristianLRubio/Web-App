#importar biblioteca
from flask import *
from flask_sqlalchemy import *

#crear objeto de la clase flask


app=Flask(__name__)

#configurar el acceso a la DB
#URL de la base de datos 
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///estudiantes.sqlite3"
#crear la DB

db=SQLAlchemy(app)

#definir las tablas de la base de datos
class Estudiante(db.Model):
    #Definir una llave primaria
    id=db.Column('id_estudiante', db.Integer, primary_key=True)
    #definir las columnas de la tabla

    nombre=db.Column(db.String(50))
    codigo=db.Column(db.String(12))

    def __init__(self, nombre, codigo):

        self.nombre=nombre
        self.codigo=codigo

@app.route('/')
def bienvenida():
    return render_template("bienvenida.html")

with app.app_context():

    db.create_all()
    app.run(debug=True)
