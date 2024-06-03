from .. import db
from datetime import datetime


class Estudiante(db.Model):
    __tablename__ = "estudiante"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable = False, default="")
    estado = db.Column(db.Boolean, default = True, nullable = False)
    
    fecha_creado = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    fecha_modificado = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    
    creado_por = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    modificado_por = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    
    
    creado_por_usuario = db.relationship("Usuario", foreign_keys= [creado_por], backref=db.backref("estudiante_usuario_creado", lazy=True))
    modificado_por_usuario = db.relationship("Usuario", foreign_keys= [modificado_por], backref=db.backref("estudiante_usuario_modificado", lazy=True))