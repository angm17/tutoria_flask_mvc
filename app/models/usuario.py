from .. import db
from datetime import datetime


class Usuario(db.Model):
    __tablename__ = "usuario"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable = False, default="")
    estado = db.Column(db.Boolean, default = True, nullable = False)
    
    fecha_creado = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    fecha_modificado = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    
    
    
