from numb3rs import validate
import pytest

def test_numbers():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("0.10.100.255") == True
    assert validate("256.256.256.256") == False
    assert validate("100") == False
    assert validate("399") == False
    assert validate("399.0.0.0") == False
    assert validate("0.399") == False
    assert validate("0.0.399") == False
    assert validate("0.0.0.399") == False
    assert validate("") == False
    assert validate("165.247.10.0.255") == False

def test_char():
    assert validate("cat") == False
    assert validate("0.cat.0.cat") == False
    assert validate("cat.0.cat.0") == False
    assert validate("cat.cat.cat.cat") == False
    assert validate("?.?.?.?") == False
