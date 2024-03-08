from jar import Jar
import pytest

def test_init():
    jar = Jar()
    jar.capacity == 12
    jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.deposit(13)
    assert jar.size == 5



def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    with pytest.raises(ValueError):
        jar.withdraw(13)
    jar.withdraw(5)
    assert jar.size == 5
