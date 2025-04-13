import logging
import os

from app import app
from routes import *  # Import all routes

if __name__ == "__main__":
    # Configura el logging
    logging.basicConfig(level=logging.DEBUG)
    
    # Muestra un mensaje claro sobre la URL en la terminal
    port = 5000
    print("\n" + "=" * 50)
    print(" 🚀 El Origen del Universo - Aplicación Web")
    print("=" * 50)
    print("\nLa aplicación está ejecutándose en:")
    print(f"➡️  URL:  http://localhost:{port}")
    print("\nAbre tu navegador y visita la URL anterior")
    print("Presiona CTRL+C para detener la aplicación")
    print("=" * 50 + "\n")
    
    # Ejecuta la aplicación para acceso local
    # Usamos 0.0.0.0 para asegurar que la conexión sea accesible en todas las interfaces
    app.run(host="0.0.0.0", port=port, debug=True)
