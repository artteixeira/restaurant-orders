import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_dishes(source_path)

    def load_dishes(self, source_path: str):
        with open(source_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name, price = row["dish"], row["price"]
                ingredient, amount = row["ingredient"], row["recipe_amount"]

                dish = self.verify_dishes(name)
                if dish:
                    dish.add_ingredient_dependency(
                        Ingredient(ingredient), int(amount))
                else:
                    dish = Dish(name, float(price))
                    dish.add_ingredient_dependency(
                        Ingredient(ingredient), int(amount))
                    self.dishes.add(dish)

    def verify_dishes(self, name):
        for dish in self.dishes:
            if dish.name == name:
                return dish
