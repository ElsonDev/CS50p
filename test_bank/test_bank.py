from bank import value
import pytest

# pytest.raises(TypeError):
    #function("arg")

def test_greeting_h():
    assert value("hi") == 20
    assert value("HI") == 20
    assert value("Hi there") == 20

def test_greeting_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello, sir") == 0


def test_greeting_no_h():
    assert value("bonjour") == 100
    assert value("allo") == 100
    assert value("Good day sir") == 100
    assert value("1") == 100
