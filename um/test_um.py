from um import count
import pytest

def test_begging():
    assert count("uM hello") == 1
    assert count("um, hello") == 1
    assert count("um.um hello") == 2
    assert count("umum hello") == 0

def test_middle():
    assert count("hello, UM, world") == 1
    assert count("hello umum world") == 0
    assert count("hello. um.um. world") == 2

def test_3_end():
    assert count("hello world um") == 1
    assert count("hello world Um um") == 2
  