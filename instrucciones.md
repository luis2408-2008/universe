# Instrucciones para ejecutar El Origen del Universo

Para ejecutar esta aplicación localmente, sigue estos pasos:

## Paso 1: Instalar dependencias
En tu terminal, ejecuta:
```bash
pip install flask flask-login flask-sqlalchemy flask-wtf email-validator gunicorn
```

## Paso 2: Ejecutar la aplicación
Simplemente ejecuta:
```bash
python main.py
```

## Paso 3: Acceder a la aplicación
Abre tu navegador y visita:
```
http://localhost:5000
```

## Credenciales predeterminadas
La aplicación crea automáticamente un usuario administrador la primera vez que se ejecuta:
- **Usuario:** admin
- **Contraseña:** admin12345
- **Email:** admin@cosmicexplorer.com

Estos datos nunca se borrarán ya que se guardan en una base de datos SQLite persistente.

## Notas importantes
- La aplicación usa SQLite en lugar de PostgreSQL para mayor facilidad
- Todos los datos se almacenan localmente en el archivo `instance/site.db`
- La base de datos y las cuentas de usuario son persistentes y no se borran al reiniciar
- La aplicación crea automáticamente contenido de ejemplo (artículos, videos e imágenes) si no existe ninguno