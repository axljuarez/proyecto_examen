from flask import Flask, render_template, request, redirect, url_for, flash
from manager import RecipeBook

app = Flask(__name__)
app.secret_key = "dev-key-recetas"

book = RecipeBook()

def seed_if_empty():
    if not book.recipes:
        r1 = book.add_recipe("Tostadas con Aguacate", "Pan tostado con aguacate y sal", servings=1, vegetarian=True)
        book.add_ingredient_to_recipe(r1.recipe_id, "Pan", "2 rebanadas")
        book.add_ingredient_to_recipe(r1.recipe_id, "Aguacate", "1")
        r2 = book.add_recipe("Ensalada César", "Ensalada clásica con aderezo César", servings=2, vegetarian=False)
        book.add_ingredient_to_recipe(r2.recipe_id, "Lechuga romana", "1 cabeza")
        book.add_ingredient_to_recipe(r2.recipe_id, "Pechuga de pollo", "200 g")

@app.route("/")
def index():
    seed_if_empty()
    total = len(book.recipes)
    return render_template("index.html", total=total)

@app.route("/recipes")
def recipes():
    seed_if_empty()
    q = request.args.get("q", "").strip()
    recipes = book.search_recipes(q) if q else book.recipes
    return render_template("recipes.html", recipes=recipes, q=q)

@app.route("/recipes/new", methods=["GET", "POST"])
def create_recipe():
    if request.method == "POST":
        try:
            title = request.form.get("title", "").strip()
            description = request.form.get("description", "").strip()
            servings = int(request.form.get("servings", "1"))
            vegetarian = bool(request.form.get("vegetarian"))
            if not title:
                raise ValueError("El título es requerido.")
            r = book.add_recipe(title, description, servings, vegetarian)
            # ingredientes opcionales
            ing_names = request.form.getlist("ing_name")
            ing_qtys = request.form.getlist("ing_qty")
            for name, qty in zip(ing_names, ing_qtys):
                if name.strip():
                    book.add_ingredient_to_recipe(r.recipe_id, name, qty)
            flash("Receta agregada.", "success")
            return redirect(url_for("recipes"))
        except Exception as e:
            flash(str(e), "error")
    return render_template("recipe_form.html", recipe=None)

@app.route("/recipes/<int:recipe_id>")
def recipe_detail(recipe_id: int):
    r = book.find_recipe_by_id(recipe_id)
    if not r:
        flash("Receta no encontrada.", "error")
        return redirect(url_for("recipes"))
    return render_template("recipe_detail.html", recipe=r)

@app.route("/recipes/<int:recipe_id>/edit", methods=["GET", "POST"])
def edit_recipe(recipe_id: int):
    r = book.find_recipe_by_id(recipe_id)
    if not r:
        flash("Receta no encontrada.", "error")
        return redirect(url_for("recipes"))
    if request.method == "POST":
        try:
            title = request.form.get("title", "").strip()
            description = request.form.get("description", "").strip()
            servings = int(request.form.get("servings", "1"))
            vegetarian = bool(request.form.get("vegetarian"))
            if not title:
                raise ValueError("El título es requerido.")
            book.update_recipe(recipe_id, title, description, servings, vegetarian)
            # reemplazamos ingredientes: borramos todos y volvemos a agregar
            r.ingredients = []
            ing_names = request.form.getlist("ing_name")
            ing_qtys = request.form.getlist("ing_qty")
            for name, qty in zip(ing_names, ing_qtys):
                if name.strip():
                    book.add_ingredient_to_recipe(recipe_id, name, qty)
            flash("Receta actualizada.", "success")
            return redirect(url_for("recipe_detail", recipe_id=recipe_id))
        except Exception as e:
            flash(str(e), "error")
    return render_template("recipe_form.html", recipe=r)

@app.route("/recipes/<int:recipe_id>/delete", methods=["POST"])
def delete_recipe(recipe_id: int):
    try:
        book.delete_recipe(recipe_id)
        flash("Receta eliminada.", "success")
    except Exception as e:
        flash(str(e), "error")
    return redirect(url_for("recipes"))

if __name__ == "__main__":
    app.run(debug=True)