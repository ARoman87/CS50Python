from fuel import convert
from fuel import gauge
import pytest


def test_conversion():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("4/4") == 100


def test_zeroDiv():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_valueError():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_fuel_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
