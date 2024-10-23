from class_methods import Pokemon

def test___str__():
    test_pokemon = Pokemon("Eevee", 37, "Normal", 2)
    test_string = test_pokemon.__str__()
    assert test_string == "Name: Eevee Type: Normal Level: 2 HP: 37"