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

## Panel de Administración
El usuario administrador tiene acceso a un panel exclusivo desde el que podrá:
- Ver estadísticas generales de la aplicación
- Monitorear los usuarios recientes
- Revisar los últimos accesos a la plataforma
- Gestionar la lista completa de usuarios registrados

Para acceder: haz clic en el botón verde "Panel Admin" en la barra de navegación (solo visible para el usuario admin).

## Gestión de Usuarios
La aplicación incluye un script para crear o actualizar usuarios manualmente:

```bash
# Para crear un nuevo usuario:
python create_user.py <nombre_usuario> <email> <contraseña>

# Ejemplo:
python create_user.py usuario1 usuario1@ejemplo.com contraseña123
```

## Persistencia de Datos
- La aplicación usa SQLite con persistencia total de datos
- Todos los datos se almacenan en `instance/cosmic_explorer.db`
- Los usuarios y contenidos **nunca se borran** entre reinicios o actualizaciones
- Si necesitas hacer una copia de seguridad, simplemente guarda el archivo de la base de datos
- Para restaurar, solo coloca el archivo de base de datos guardado en la carpeta `instance`

## Notas técnicas
- La aplicación está optimizada para funcionar sin necesidad de configuración especial
- Las sesiones de usuario persisten entre reinicios
- Contenido generado automáticamente para demostración (artículos, videos e imágenes)