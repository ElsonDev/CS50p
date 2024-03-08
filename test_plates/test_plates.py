from plates import is_valid

def test_start_letters():
    assert is_valid("BEGIN") == True
    assert is_valid("50BEGIN") == False
    assert is_valid("A5") == False


def test_minmax():
    assert is_valid("B") == False
    assert is_valid("BB") == True
    assert is_valid("BEGINNING") == False

def test_numbers():
    assert is_valid("05BEG") == False
    assert is_valid("50BEG") == False
    assert is_valid("BEG05") == False
    assert is_valid("BEG50") == True
    assert is_valid("BEG50S") == False


def test_punctuation_spaces():
    assert is_valid("BE GIN") == False
    assert is_valid("BE,GIN") == False
    assert is_valid("BEGIN!") == False
    assert is_valid("BE3.14") == False