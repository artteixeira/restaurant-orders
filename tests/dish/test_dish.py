from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest

# Req 2
def test_dish():
    pizza = Dish("Pizza", 30.0)
    pizza2 = Dish("Pizza", 30.0)
    strogonoff = Dish("Strogonoff", 30.0)

    assert pizza.name == "Pizza"

    assert pizza.__hash__() == pizza2.__hash__()
    assert pizza.__hash__() != strogonoff.__hash__()

    assert pizza.__eq__(pizza2) is True
    assert pizza.__eq__(strogonoff) is False

    assert pizza.__repr__() == "Dish('Pizza', R$30.00)"

    with pytest.raises(TypeError):
        Dish("Pizza", "30.0")

    with pytest.raises(ValueError):
        Dish("Pizza", 0)

    pizza.add_ingredient_dependency(Ingredient("ovo"), 2)

    assert pizza.recipe.get(Ingredient("ovo")) == 2

    assert pizza.get_restrictions() == {
        Restriction.ANIMAL_DERIVED}

    assert pizza.get_ingredients() == {Ingredient("ovo")}