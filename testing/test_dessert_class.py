from dessert_class import (
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_string():
    test_item = DessertItem("Cookie")
    test_string = test_item.__str__()
    assert test_string == "The dessert is Cookie."