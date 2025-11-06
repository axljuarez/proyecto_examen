from dataclasses import dataclass, field
from typing import List

@dataclass
class Ingredient:
    name: str
    quantity: str = ""  # e.g., "2 cups", "1 tsp"

@dataclass
class Recipe:
    recipe_id: int
    title: str
    description: str = ""
    ingredients: List[Ingredient] = field(default_factory=list)
    servings: int = 1
    vegetarian: bool = False

    def add_ingredient(self, name: str, quantity: str = ""):
        name = name.strip()
        if not name:
            raise ValueError("El nombre del ingrediente no puede estar vacío.")
        self.ingredients.append(Ingredient(name=name, quantity=quantity.strip()))

    def remove_ingredient(self, name: str):
        name = name.strip().lower()
        before = len(self.ingredients)
        self.ingredients = [i for i in self.ingredients if i.name.lower() != name]
        if len(self.ingredients) == before:
            raise ValueError("Ingrediente no encontrado en la receta.")