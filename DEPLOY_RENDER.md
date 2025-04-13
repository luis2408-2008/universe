# Guía para Desplegar en Render

Este documento contiene las instrucciones paso a paso para desplegar la aplicación "El Origen del Universo" en la plataforma Render.com.

## Requisitos previos

1. Tener una cuenta en [Render.com](https://render.com)
2. Tener el código de la aplicación en un repositorio Git (GitHub, GitLab, etc.)

## Paso 1: Crear una base de datos PostgreSQL en Render

1. Inicia sesión en tu cuenta de Render
2. Ve a la sección "Databases" (Bases de datos)
3. Haz clic en "New PostgreSQL"
4. Configura la base de datos:
   - Nombre: `cosmic-explorer-db` (o el nombre que prefieras)
   - Plan: Elige el plan gratuito o el que mejor se adapte a tus necesidades
   - Región: Selecciona la región más cercana a tus usuarios
5. Haz clic en "Create Database"
6. Espera a que la base de datos se cree y esté lista (puede tardar unos minutos)
7. Una vez creada, guarda los siguientes datos que necesitarás más adelante:
   - Internal Database URL
   - External Database URL
   - Username
   - Password

## Paso 2: Crear el servicio web en Render

1. En el panel de Render, ve a la sección "Web Services"
2. Haz clic en "New Web Service"
3. Conecta tu repositorio de Git
4. Configura el servicio web:
   - Nombre: `cosmic-explorer` (o el nombre que prefieras)
   - Entorno: Python
   - Plan: Elige el plan gratuito o el que mejor se adapte a tus necesidades
   - Región: Selecciona la misma región que escogiste para la base de datos
   - Branch: `main` (o la rama que uses)
   - Build Command: `pip install -r render_requirements.txt && ./install_postgresql.sh`
   - Start Command: `gunicorn main:app`

## Paso 3: Configurar variables de entorno

1. En la configuración del servicio web, busca la sección "Environment Variables"
2. Añade las siguientes variables:
   - `DATABASE_URL`: Copia el valor de "Internal Database URL" de tu base de datos
   - `SECRET_KEY`: Inventa una clave secreta larga y aleatoria (recomendado: al menos 32 caracteres)
   - `ADMIN_USERNAME`: El nombre de usuario que quieras para el administrador (por defecto: "admin")
   - `ADMIN_PASSWORD`: La contraseña que quieras para el administrador (por defecto: "admin12345")
   - `ADMIN_EMAIL`: El correo electrónico que quieras para el administrador

## Paso 4: Desplegar la aplicación

1. Haz clic en "Create Web Service"
2. Espera a que Render despliegue tu aplicación (puede tardar algunos minutos la primera vez)
3. Una vez completado, tu aplicación estará disponible en la URL proporcionada por Render

## Paso 5: Verificar la instalación

1. Visita la URL de tu aplicación
2. Deberías ver la página de inicio de "El Origen del Universo"
3. Inicia sesión con el usuario administrador que configuraste
4. Verifica que puedes acceder al panel de administración

## Solución de problemas comunes

### La base de datos no se conecta
- Verifica que la variable `DATABASE_URL` sea correcta
- Asegúrate de que la base de datos esté en estado "Available" en Render

### No se crea el usuario administrador
- Verifica los logs en la sección "Logs" de tu servicio web
- Ejecuta manualmente el script `init_admin.py` desde la consola de Render

### La aplicación no carga correctamente
- Revisa los logs para identificar errores
- Verifica que todos los archivos estáticos se estén cargando correctamente

### Cambiar la contraseña del administrador después del despliegue
1. Accede a la consola de Render para tu servicio web
2. Ejecuta: `python create_user.py admin nuevo_email nueva_contraseña`

## Notas importantes

- La migración de datos desde SQLite a PostgreSQL no es automática. Los usuarios y contenidos se crearán desde cero en el despliegue.
- Se recomienda realizar copias de seguridad periódicas de la base de datos en producción.
- Para más opciones de configuración, consulta la documentación de Render.