from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    sal = Ingredient("sal")
    sal2 = Ingredient("sal")
    presunto = Ingredient("presunto")

    assert sal.__hash__() == sal2.__hash__()
    assert sal.__hash__() != presunto.__hash__()

    assert sal.__eq__(sal2) is True
    assert sal.__eq__(presunto) is False

    assert sal.name == "sal"

    assert presunto.restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT}

    assert sal.__repr__() == "Ingredient('sal')"
