from twttr import shorten


def test_regular():
    assert shorten("Hello World!") == "Hll Wrld!"


def test_lowerCaps():
    assert shorten("tw1tter") == "tw1ttr"


def test_caps():
    assert shorten("ANGEL") == "NGL"
