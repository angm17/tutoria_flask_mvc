from flask import Blueprint, render_template


usuario = Blueprint('usuario', __name__, static_folder='static')

@usuario.route('/')
def index():
    # users = User.query.all()
    return render_template('base.html')