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

## Notas importantes
- La aplicación ahora usa SQLite en lugar de PostgreSQL para mayor facilidad
- Todos los datos se almacenan localmente en el archivo `site.db`
- La clave secreta está configurada directamente en el código