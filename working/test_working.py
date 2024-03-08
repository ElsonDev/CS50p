from working import convert
import pytest

def test_hours_am_to():
    #assert convert("11:00 AM to 10:00 PM") == "11:00 to 22:00"
    assert convert("9:59 AM to 5:23 PM") == "09:59 to 17:23"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_hours_pm_to():
    assert convert("11:00 PM to 12:00 AM") == "23:00 to 00:00"
    #assert convert("11:30 PM to 12:20 PM") == "23:30 to 12:20"
    #assert convert("5 PM to 9 AM") == "17:00 to 09:00"
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_valueerror():
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"
    with pytest.raises(ValueError):
        convert("9:69 AM to 5:23 PM")










