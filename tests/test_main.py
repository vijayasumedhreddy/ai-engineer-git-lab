from app.main import greet


def test_greet():
    assert greet("Sumedh") == "Hello, Sumedh!"


def test_greet_spanish():
    assert greet("Sumedh", "Spanish") == "Hola, Sumedh!"


def test_greet_french():
    assert greet("Sumedh", "French") == "Bonjour, Sumedh!"