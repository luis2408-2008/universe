"""
Script para crear un usuario manualmente en la base de datos
"""
import os
import sys
from app import app, db
from models import Usuario

def crear_usuario(username, email, password):
    """Crea un usuario en la base de datos o actualiza si ya existe"""
    with app.app_context():
        # Verificar si el usuario ya existe
        usuario_existente = Usuario.query.filter_by(username=username).first()
        
        if usuario_existente:
            print(f"El usuario '{username}' ya existe. Actualizando contraseña...")
            usuario_existente.set_password(password)
            db.session.commit()
            print(f"¡Contraseña actualizada para '{username}'!")
            return
        
        # Crear nuevo usuario
        nuevo_usuario = Usuario(
            username=username,
            email=email
        )
        nuevo_usuario.set_password(password)
        
        # Guardar en la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        print(f"¡Usuario '{username}' creado con éxito!")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python create_user.py <nombre_usuario> <email> <contraseña>")
        sys.exit(1)
    
    username = sys.argv[1]
    email = sys.argv[2]
    password = sys.argv[3]
    
    crear_usuario(username, email, password)