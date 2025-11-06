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
