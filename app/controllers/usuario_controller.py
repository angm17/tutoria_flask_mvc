from flask import Blueprint, render_template, request, redirect

from ..models import Usuario
from .. import db


usuario = Blueprint('usuario', __name__, static_folder='static')

@usuario.route('/')
def index():
    users = Usuario.query.all()
    return render_template('usuario.html', tituloPagina="Usuarios", usuarios = users)

@usuario.route('/guardar', methods=["POST"])
def guardar():
    nombres = request.form["nombres"]
    estado = request.form["estado"]
    
    estado = bool(int(estado)) if estado is not None else False
    

    usuario = Usuario(
        nombre = nombres,
        estado = estado
    )
    
    db.session.add(usuario)
    
    try:
        db.session.commit()
        return redirect("/usuarios")
    except Exception as e:
        db.session.rollback()
    

# def actualizar():
#     pass

# def eliminar():
#     pass

# def listar():
#     pass

# def listarTodos():
#     pass
