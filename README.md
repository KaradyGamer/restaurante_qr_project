# 🍽️ Restaurante QR Project

Sistema web para la gestión de pedidos mediante código QR en restaurantes. Permite a los clientes hacer pedidos desde el menú, y al personal gestionar los mismos.

---

## 🚀 Requisitos previos

Asegúrate de tener instalado:

- Python 3.10 o superior
- Git

---

## ⚙️ Instalación del entorno (desarrollo local)

1. **Clona el repositorio:**

```bash
git clone https://github.com/KaradyGamer/restaurante_qr_project.git
cd restaurante_qr_project
```
2. Crear y activa un entrono virtual
**Windows**
```bash
python -m venv env
env\Scripts\activate
```
**Linux / Mac**
```bash
python3 -m venv env
source env/bin/activate
```
## 3. Instala las dependencias:
```bash
python3 -m venv env
source env/bin/activate
```
**Si aún no tienes el archivo requirements.txt, puedes generarlo así:**
```bash
pip freeze > requirements.txt
```
# 🛠️ Configuración inicial
**1. Aplica migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```
**2. crea un superusuario()**
```bash
python manage.py createsuperuser
```
**3. Ejecuta el servidor:**
```bash
python manage.py runserver
```
git add README.md
git commit -m "Agregado archivo README con instrucciones"
git push origin main
```

¿Te gustaría que te dé también el contenido de `requirements.txt` basado en lo que ya tienes instalado?
