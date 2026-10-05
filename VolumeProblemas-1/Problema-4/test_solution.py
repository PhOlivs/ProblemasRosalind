from solution import rabbit_pairs


def test_sample():
    assert rabbit_pairs(5, 3) == 19


def test_first_month():
    assert rabbit_pairs(1, 3) == 1


def test_second_month():
    assert rabbit_pairs(2, 3) == 1


def test_fibonacci_case():
    assert rabbit_pairs(6, 1) == 8


def test_two_offspring():
    assert rabbit_pairs(5, 2) == 11
