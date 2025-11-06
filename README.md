# Recetario Flask (POO + CRUD)

Pequeña aplicación Flask para gestionar recetas con un enfoque POO.

Requisitos
- Python 3.10+
- pip

Instalación y ejecución
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt

# Ejecutar app
export FLASK_APP=app.py       # Windows: set FLASK_APP=app.py
flask run
# o
python app.py
```

Qué incluye
- CRUD completo para recetas (crear, leer, actualizar, borrar).
- Modelos con dataclasses (Recipe, Ingredient).
- Lógica central en RecipeBook (manager).
- Plantillas Jinja2 simples.
- Ejemplos iniciales con seed_if_empty.

Subir a GitHub (ejemplo con 2 commits mínimos)
1. Inicializar repo y primer commit (versión base):
```bash
git init
git add .
git commit -m "chore: proyecto base - recetario inicial"
```
2. Hacer cambios relevantes y segundo commit (añadir CRUD, plantillas, mejoras):
```bash
# realizar cambios (por ejemplo ajustar rutas o templates)
git add .
git commit -m "feat: agregar CRUD para recetas y plantilla básica"
```
3. Crear repo en GitHub (p. ej. `recetario-flask`), luego:
```bash
git remote add origin https://github.com/<TU_USUARIO>/recetario-flask.git
git branch -M main
git push -u origin main
```

Si quieres, puedo generarte los comandos exactos o ayudarte a crear el repo si me das el permiso y los datos (usuario/repo).  