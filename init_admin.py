"""
Este script crea el usuario administrador en el entorno de producción.
Se ejecutará al iniciar el servidor en Render.
"""
import os
from app import app, db
from models import Usuario

def crear_admin():
    with app.app_context():
        # Verificar si existe el usuario administrador
        admin_username = os.environ.get("ADMIN_USERNAME", "admin")
        admin_email = os.environ.get("ADMIN_EMAIL", "admin@cosmicexplorer.com")
        admin_password = os.environ.get("ADMIN_PASSWORD", "admin12345")
        
        admin_exists = Usuario.query.filter_by(username=admin_username).first()
        if not admin_exists:
            admin_user = Usuario(
                username=admin_username,
                email=admin_email
            )
            admin_user.set_password(admin_password)
            db.session.add(admin_user)
            db.session.commit()
            print(f"Usuario administrador '{admin_username}' creado con éxito en producción")
        else:
            print(f"Usuario administrador '{admin_username}' ya existe en la base de datos")

if __name__ == "__main__":
    crear_admin()