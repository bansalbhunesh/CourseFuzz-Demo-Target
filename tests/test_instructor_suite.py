from solution import classify_triangle


def test_equilateral() -> None:
    assert classify_triangle(3, 3, 3) == "equilateral"


def test_scalene() -> None:
    assert classify_triangle(3, 4, 5) == "scalene"


def test_degenerate() -> None:
    assert classify_triangle(1, 2, 3) == "invalid"


def test_non_positive() -> None:
    assert classify_triangle(0, 2, 2) == "invalid"


def test_isosceles_first_pair() -> None:
    assert classify_triangle(2, 2, 3) == "isosceles"
