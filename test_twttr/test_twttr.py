from twttr import shorten

def test_upper():
    assert shorten("HELLO") == "HLL"
    assert shorten("MY NAME IS STEVE!") == "MY NM S STV!"
    assert shorten("I HAVE 5 APPLES") == " HV 5 PPLS"


def test_lower():
    assert shorten("hello") == "hll"
    assert shorten("my name is steve!") == "my nm s stv!"
    assert shorten("i have 5 apples") == " hv 5 ppls"