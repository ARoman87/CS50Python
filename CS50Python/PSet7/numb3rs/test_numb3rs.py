from numb3rs import validate
import pytest


def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.1") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False


def test_validate_first():
    assert validate("1.512.512.512") == False
