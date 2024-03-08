from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("2/3") == 67
    with pytest.raises(ValueError):
        convert("cat/0")
    with pytest.raises(ValueError):
        convert("0/cat")
    with pytest.raises(ValueError):
        convert("10/5")
    with pytest.raises(ZeroDivisionError):
        convert("75/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"
