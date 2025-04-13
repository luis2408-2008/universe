import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
# Create the app
app = Flask(__name__)
app.secret_key = "clave_secreta_para_tu_aplicacion"

# Configure the database to use SQLite en una ubicación permanente
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'cosmic_explorer.db')
# Asegurarnos de que el directorio existe
os.makedirs(os.path.dirname(db_path), exist_ok=True)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the app with the extension
db.init_app(app)

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor inicia sesión para acceder a esta página.'

with app.app_context():
    # Import models here so their tables are created
    import models  # noqa: F401
    
    @login_manager.user_loader
    def load_user(user_id):
        from models import Usuario
        return Usuario.query.get(int(user_id))

    # En vez de recrear tablas, verificamos y creamos solo las que faltan
    # Esto preserva los datos existentes
    from sqlalchemy import inspect
    inspector = inspect(db.engine)
    existing_tables = inspector.get_table_names()
    
    if not existing_tables:
        # Solo crear tablas si no existen (primera ejecución)
        print("Creando tablas por primera vez...")
        db.create_all()
    else:
        print(f"Base de datos encontrada con {len(existing_tables)} tablas. Manteniendo datos existentes.")
