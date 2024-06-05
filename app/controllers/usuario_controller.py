from flask import Blueprint, render_template, request, redirect

from ..models import Usuario
from .. import db


usuario = Blueprint('usuario', __name__, static_folder='static')

@usuario.route('/')
def index():
    users = Usuario.query.all()
    return render_template('usuario/usuario.html', tituloPagina="Usuarios", usuarios = users)

@usuario.route('/add')
def add():
    return render_template('usuario/crear.html', tituloPagina="Añadir un Usuario")

@usuario.route('/edit/<int:id>')
def edit(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return redirect("/usuarios")
    return render_template('usuario/editar.html', tituloPagina="Editar un Usuario", usuario = usuario)


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

@usuario.route('/guardar-editar', methods=["POST"])
def guardar_editar():
    id = request.form["id"]
    
    usuario = Usuario.query.get(id)
    if not usuario:
        return redirect("/usuarios")
    
    
    nombres = request.form["nombres"]
    estado = request.form["estado"]
    
    estado = bool(int(estado)) if estado is not None else False
    
    usuario.nombre = nombres
    usuario.estado = estado
    # db.session.add(usuario)
    try:
        db.session.commit()
        return redirect("/usuarios")
    except Exception as e:
        db.session.rollback()


@usuario.route('/eliminar/<int:id>', methods=["POST"])
def eliminar(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return redirect("/usuarios")

    usuario.estado = False
    
    # db.session.delete(usuario)
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
