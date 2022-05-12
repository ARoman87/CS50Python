from bank import value


def test_greetZero():
    assert value("Hello") == 0


def test_greetTwenty():
    assert value("hi") == 20


def test_greet_oneHundred():
    assert value("Whats up") == 100
