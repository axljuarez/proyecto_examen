from typing import List, Optional
from models import Recipe, Ingredient

class RecipeBook:
    def __init__(self):
        self.recipes: List[Recipe] = []

    # ---- CRUD Recetas ----
    def add_recipe(self, title: str, description: str = "", servings: int = 1, vegetarian: bool = False) -> Recipe:
        new_id = (max([r.recipe_id for r in self.recipes]) + 1) if self.recipes else 1
        recipe = Recipe(recipe_id=new_id, title=title.strip(), description=description.strip(),
                        servings=int(servings), vegetarian=bool(vegetarian))
        self.recipes.append(recipe)
        return recipe

    def find_recipe_by_id(self, recipe_id: int) -> Optional[Recipe]:
        return next((r for r in self.recipes if r.recipe_id == recipe_id), None)

    def search_recipes(self, query: str) -> List[Recipe]:
        q = query.lower().strip()
        return [r for r in self.recipes if q in r.title.lower() or q in r.description.lower()]

    def update_recipe(self, recipe_id: int, title: str, description: str, servings: int, vegetarian: bool) -> Recipe:
        r = self.find_recipe_by_id(recipe_id)
        if not r:
            raise ValueError("Receta no encontrada.")
        r.title = title.strip()
        r.description = description.strip()
        r.servings = int(servings)
        r.vegetarian = bool(vegetarian)
        return r

    def delete_recipe(self, recipe_id: int) -> None:
        r = self.find_recipe_by_id(recipe_id)
        if not r:
            raise ValueError("Receta no encontrada.")
        self.recipes = [rec for rec in self.recipes if rec.recipe_id != recipe_id]

    # helpers para ingredientes sobre receta
    def add_ingredient_to_recipe(self, recipe_id: int, name: str, quantity: str = ""):
        r = self.find_recipe_by_id(recipe_id)
        if not r:
            raise ValueError("Receta no encontrada.")
        r.add_ingredient(name, quantity)

    def remove_ingredient_from_recipe(self, recipe_id: int, name: str):
        r = self.find_recipe_by_id(recipe_id)
        if not r:
            raise ValueError("Receta no encontrada.")
        r.remove_ingredient(name)