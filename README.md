# Biblioteca Django

## Ejecutar localmente

> **Requisito:** Sistema UNIX-like (Linux, macOS) o WSL en Windows.

Primero que todo debemos ubicarnos en nuestro repositorio clonado.

### 1. Instalar dependencias del sistema

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3.12-venv
```

### 2. Crear y activar el entorno virtual

```bash
# Crear el entorno virtual en python 3 (**venv** es la ruta donde queramos poner nuestro venv)
python3 -m venv venv

# Activarlo
source venv/bin/activate
```

### 3. Instalar dependencias del proyecto

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

```bash
# Aplicar migraciones
./manage.py migrate

# Poblar con datos iniciales
./manage.py shell < biblioteca/poblar_datos.py
```

### 5. Crear superusuario

```bash
./manage.py createsuperuser
```

### 6. Iniciar el servidor

```bash
./manage.py runserver
```

### 7. Acceder al panel de administración

Abre tu navegador en: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

Inicia sesión con las credenciales del superusuario que creaste y vemos la vista de Admin junto a los modelos creados.

---
