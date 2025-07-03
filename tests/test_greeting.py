from notebooks.my_fabric_notebook import greet_name

def test_greet_name_simple():
    """Verify that greet_name returns the correct greeting."""
    assert greet_name("World") == "Hello, World!"