from solution import classify_triangle


def test_coursefuzz_classify_triangle_a19d63ef():
    assert classify_triangle(1, 2, 2) == 'isosceles'
