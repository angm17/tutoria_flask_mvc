from flask import Blueprint, render_template
# from app.models.user import User

home = Blueprint('home', __name__, static_folder='static')

@home.route('/')
def index():
    # users = User.query.all()
    return render_template('inicio.html', tituloPagina = "Inicio")