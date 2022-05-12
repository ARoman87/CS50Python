from plates import is_valid


def test_plates():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("AAA22A") == False
    assert is_valid("H") == False
    assert is_valid("12345") == False


def alpha_check():
    assert is_valid("50CS") == False


def test_endDigit():
    assert is_valid("PI3.14") == False


def nothing():
    assert is_valid("") == False
