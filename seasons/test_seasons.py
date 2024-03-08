from seasons import convert
import pytest

def test_date():
    assert convert("2022-10-21") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2021-10-21") == "One million, fifty-one thousand, two hundred minutes"
    assert convert("2016-02-29") == "Four million, nineteen thousand forty minutes"








