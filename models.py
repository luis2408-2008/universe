from datetime import datetime

from app import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    ultimo_acceso = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Usuario {self.username}>'


class ContenidoCosmico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)  # big_bang, theories, philosophy, space_time
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ContenidoCosmico {self.titulo}>'


class VideoCosmico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    youtube_id = db.Column(db.String(20), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f'<VideoCosmico {self.titulo}>'


class ImagenCosmica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    url = db.Column(db.String(255), nullable=False)
    fuente = db.Column(db.String(100))
    categoria = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f'<ImagenCosmica {self.titulo}>'
