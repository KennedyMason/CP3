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

def test_candy():
    test_item = Candy("Lollipop", 20, 5.00)
    assert test_item.name == "Lollipop"
    assert test_item.candy_weight == 20
    assert test_item.price_per_pound == 5.00
  
def test_cookie():
    test_item = Cookie("Snickerdoodle", 12, 10.00)
    assert test_item.name == "Snickerdoodle"
    assert test_item.cookie_quantity == 12
    assert test_item.price_per_dozen == 10.00

def test_ice_cream():
    test_item = IceCream("Vanilla", 3, 2.00)
    assert test_item.name == "Vanilla"
    assert test_item.scoop_count == 3
    assert test_item.price_per_scoop == 2.00

def test_sundae():
    test_item = Sundae("Vanilla", 3, 2.00, "Cherry", 0.50)
    assert test_item.name == "Vanilla"
    assert test_item.scoop_count == 3
    assert test_item.price_per_scoop == 2.00
    assert test_item.topping_name == "Cherry"
    assert test_item.topping_price == 0.50



