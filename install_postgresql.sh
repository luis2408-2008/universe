#!/bin/bash

# Instalar paquetes de PostgreSQL para conectarse a la base de datos
apt-get update
apt-get install -y libpq-dev

# Instalar la dependencia psycopg2 para Python
pip install psycopg2-binary

# Ejecutar el script para crear el usuario administrador
python init_admin.py

echo "Preparación para PostgreSQL completada con éxito"